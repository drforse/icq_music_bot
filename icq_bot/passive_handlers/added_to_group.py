from bot.event import Event
from ..db_service import DB
from ..core import Command


class AddedToGroup(Command):
    def __init__(self):
        super().__init__()

    def execute(self, bot, event: Event):
        if bot.token.split(':')[-1] in [i['userId'] for i in event.data['newMembers']]:
            DB().save_group(event.data['chat']['chatId'])
