from ..core import Command
from bot.event import Event
from music_downloader import Search as SearchMusic
import json


class Search(Command):
    def __init__(self):
        super().__init__()

    def execute(self, bot, event: Event):
        chat_id = event.data['chat']['chatId']
        text = event.data['text']
        reply = list(filter(lambda i: i['type'] == 'reply', event.data.get('parts') or []))
        if len(text.split()) > 1:
            search_query = text.split(maxsplit=1)[1]
        elif reply:
            search_query = reply[0]['payload']['message']['text']
        else:
            self._bot.send_text(chat_id, 'You should provide an argument to the command or reply to a text message')
            return

        if not search_query:
            self._bot.send_text(chat_id, 'You should provide an argument to the command or reply to a text message')
            return

        sm = SearchMusic(search_query)
        results = sm.get_results(maxResults=10, videoDuration='medium')
        kb = []
        for result in results:
            kb.append([{'text': result.title, 'callbackData': f'youtube_music {result.id}'}])
        kb = json.dumps(kb)

        self._bot.send_text(chat_id=chat_id, text=search_query, inline_keyboard_markup=kb)
