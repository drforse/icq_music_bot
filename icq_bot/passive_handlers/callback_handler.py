from ..core import Command
from bot.event import Event
from music_downloader.types import MusicFile
from bot.handler import BotButtonCommandHandler
from ..db_service import DB


class CallbackHandler(Command):
    def __init__(self):
        super().__init__()

    def execute(self, bot, event: Event):
        db = DB()
        chat_id = event.data['message']['chat']['chatId']
        music_id = event.data['callbackData'].split()[-1]

        file_id = db.find_music(music_id)
        if file_id:
            bot.send_voice(chat_id, file_id)
            return

        mfile = MusicFile(f'music_files/{music_id}')
        mfile.download(f'https://music.youtube.com/watch?v={music_id}')
        file_id = bot.send_audio(mfile.path+'.mp3', chat_id)

        db.save_music(music_id, file_id)

        bot.answer_callback_query(event.data['queryId'], text='', show_alert=False)

    def register(self, filters=None, command: str = None):
        self._dp.add_handler(BotButtonCommandHandler(callback=self.execute))
