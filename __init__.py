from icq_bot.main import bot
from bot.handler import NewChatMembersHandler
from icq_bot.passive_handlers import *
from icq_bot.user_commands import Start
from bot.filter import Filter
import logging


logging.basicConfig(level=logging.INFO)


Start().register(command='start')
MusicFiles().register(filters=Filter.file)
AddedToGroup().register(handler=NewChatMembersHandler)


bot.start_polling()
