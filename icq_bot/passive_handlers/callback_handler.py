from ..core import Command
from bot.event import Event
from music_downloader.types import MusicFile
from bot.handler import BotButtonCommandHandler


class CallbackHandler(Command):
    def __init__(self):
        super().__init__()

    def execute(self, bot, event: Event):
        music_id = event.data['callbackData'].split()[-1]
        mfile = MusicFile(f'music_files/{music_id}')
        mfile.download(f'https://music.youtube.com/watch?v={music_id}')
        bot.send_audio(mfile.path+'.mp3', event.data['message']['chat']['chatId'])
        bot.answer_callback_query(event.data['queryId'])

    def register(self, filters=None, command: str = None):
        self._dp.add_handler(BotButtonCommandHandler(callback=self.execute))
