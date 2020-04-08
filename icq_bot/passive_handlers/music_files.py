from ..core import Command
from bot.event import Event
import pathlib
import logging


class MusicFiles(Command):
    def __init__(self):
        super().__init__()

    def execute(self, bot, event: Event):
        logging.debug('handled a file')
        file_info = self._bot.get_file_info(file_id=event.data['parts'][0]['payload']['fileId'])
        formats = ('.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dct',
                   '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mp3', '.mpc',
                   '.msv', '.nmf', '.nsf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.raw', '.rf64', '.sln',
                   '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', '.webm', '.8svx', '.cda')
        if True not in [file_info['file_name'].endswith(f) for f in formats]:
            logging.debug('%s is not audio, so not continuing...' % file_info['file_name'])
            return
        file_path = self._bot.download_file(file_id=event.data['parts'][0]['payload']['fileId'],
                                            path=pathlib.Path.cwd() / pathlib.Path('music_files'))
        self._bot.send_audio(file_path, event.data['chat']['chatId'])
