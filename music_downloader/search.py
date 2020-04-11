from config import *
import requests
import typing
from .types import SearchResult


class Search:

    __api_key = GOOGLE_SEARCH_API_KEY
    __url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&type=video&key={__api_key}&fields=items'

    def __init__(self, q: str):
        self.q = q
        self.results = []
        self._results = None

    def get_results(self, offset: int = 0, **kwargs) -> typing.List[SearchResult]:
        url = self.__url % self.q
        for kw in kwargs:
            url += f'&{kw}={kwargs[kw]}'
        r = requests.get(url)
        self._results = r.json()
        self.results = [SearchResult(res) for res in self._results['items'][offset:]]
        return self.results

    # async def get_filtered_results(self, func: typing.Callable = None, *args, **kwargs):
    #     results = self.results or await self.get_results()
    #     if not func:
    #         func = self.default_filter
    #         args = [self.q, ]
    #     return [res for res in results if await func(res, *args, **kwargs)]
    #
    # @staticmethod
    # async def default_filter(res: SearchResult, *args, **kwargs):
    #     print(args[0], res.title)
    #     if args[0].lower() in res.title.lower():
    #         return True
    #     return False
