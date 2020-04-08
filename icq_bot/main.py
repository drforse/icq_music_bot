from bot.bot import Bot
from config import bot_token
import io
import requests
import pathlib
import typing
import logging


class Bot(Bot):
    def __init__(self, token, api_url_base=None, name=None, version=None, timeout_s=20, poll_time_s=60):
        super().__init__(token, api_url_base=api_url_base, name=name, version=version,
                         timeout_s=timeout_s, poll_time_s=poll_time_s)

    def get_file_info(self, file_id: str):
        get_file_info_url = f'https://u.icq.net/files/api/v1.1/info/%s?aimsid={self.token}'
        r = requests.get(get_file_info_url % file_id)
        result = r.json()
        file_info = result['result']['info']
        return file_info

    def download_file(self, file_id: str, path: typing.Union[pathlib.WindowsPath, pathlib.PosixPath, str] = None,
                      name: str = None) -> pathlib.WindowsPath:
        if type(path) == str:
            path = pathlib.Path(path)
        elif not path:
            path = pathlib.Path.cwd()
        file_info = self.get_file_info(file_id)
        file_name = name or file_info['file_name']
        file_dlink = file_info['dlink']
        logging.debug('%s is loading...' % file_name)
        r = requests.get(file_dlink)
        with open(path / file_name, 'wb') as f:
            f.write(r.content)
        logging.debug('%s is loaded.' % file_name)
        return path / file_name

    def send_audio(self, file: typing.Union[int, pathlib.WindowsPath, pathlib.PosixPath,
                                            str, io.BytesIO, io.FileIO], chat_id):
        logging.debug('sending %s' % file)
        if type(file) == io.BytesIO:
            file.name = "hello_voice.mp3"
            file.seek(0)
            result = bot.send_voice(chat_id, file=file.read())
            logging.debug('%s sent' % file)
            return result.json()['fileId']
        if type(file) == int:
            result = bot.send_voice(chat_id, file=file)
            logging.debug('%s sent' % file)
            return result.json()['fileId']

        def _send_fileio(file):
            file = io.BytesIO(file.read())
            file.name = "hello_voice.mp3"
            file.seek(0)
            result = bot.send_voice(chat_id, file=file.read())
            logging.debug('%s sent' % file)
            return result.json()['fileId']
        if type(file) in (pathlib.WindowsPath, pathlib.PosixPath) or type(file) == str:
            with open(file, 'rb') as f:
                return _send_fileio(f)
        if type(file) == io.FileIO:
            return _send_fileio(file)


bot = Bot(token=bot_token)
