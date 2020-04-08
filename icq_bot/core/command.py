from ..main import bot
from bot.event import Event
from bot.handler import MessageHandler, CommandHandler


class Command:
    def __init__(self):
        self._bot = bot
        self._dp = bot.dispatcher

    def execute(self, bot, event: Event):
        pass

    def register(self, filters=None, command: str = None, handler=None, **kwargs):
        if handler:
            return self._dp.add_handler(handler(callback=self.execute, **kwargs))
        if command:
            return self._dp.add_handler(CommandHandler(command=command, filters=filters, callback=self.execute))
        return self._dp.add_handler(MessageHandler(filters=filters, callback=self.execute))
