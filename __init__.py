from icq_bot.main import bot
from icq_bot.passive_handlers import MusicFiles
from bot.filter import Filter
import logging


logging.basicConfig(level=logging.DEBUG)


MusicFiles().register(filters=Filter.file)


bot.start_polling()
