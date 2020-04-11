from ..core import Command
from bot.event import Event
from ..db_service import DB


class Start(Command):
    def __init__(self):
        super().__init__()

    def execute(self, bot, event: Event):
        if event.data['chat']['type'] == 'private':
            DB().save_user(event.data['chat']['chatId'])
        else:
            DB().save_group(event.data['chat']['chatId'])
        bot.send_text(chat_id=event.data['chat']['chatId'],
                      text='Hello! I am bot for automatic transfering music files into voices ('
                           'so you can listen it directly in the app) and also downloading music from YouTube\n'
                           'Just send me an audio file and I will transfer it or'
                           'you can add me in a group and I will transfer every new music file\n'
                           'Or, if you want search YouTube for music, send /search <name>\n\n'
                           'My developer: @dr_forse')
