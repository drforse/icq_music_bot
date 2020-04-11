from icq_bot.main import bot
from icq_bot.passive_handlers import *
from icq_bot.user_commands import *
from bot.filter import Filter
from bot.handler import NewChatMembersHandler
import logging


logging.basicConfig(level=logging.INFO)


Start().register(command='start')
MusicFiles().register(filters=Filter.file)
AddedToGroup().register(handler=NewChatMembersHandler)
Search().register(command='search')
CallbackHandler().register()


bot.start_polling()
