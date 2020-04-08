from ..main import bot
from bot.event import Event
from bot.handler import MessageHandler


class Command:
    def __init__(self):
        self._bot = bot
        self._dp = bot.dispatcher

    def execute(self, bot, event: Event):
        pass

    def register(self, filters=None):
        self._dp.add_handler(MessageHandler(filters=filters, callback=self.execute))
