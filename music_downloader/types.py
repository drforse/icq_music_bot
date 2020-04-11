import youtube_dl


class MusicFile:
    def __init__(self, path: str = None):
        self.path = path
        params = {'format': 'bestaudio/best',
                  'postprocessors': [{
                      'key': 'FFmpegExtractAudio',
                      'preferredcodec': 'mp3',
                      'preferredquality': '192',
                  }]
                  }
        if path:
            params.update({'outtmpl': f'{path}.%(ext)s'})
        self.dl = youtube_dl.YoutubeDL(params=params)

    def download(self, url: str):
        return self.dl.extract_info(url=url, download=True)


class SearchResult:
    def __init__(self, result: dict):
        self._result = result
        self.id = result['id']['videoId']
        snippet = result['snippet']
        self.title = snippet.get('title')

