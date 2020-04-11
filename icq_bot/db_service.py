from pymongo import MongoClient
from config import mongo_address


client = MongoClient(mongo_address)
db = client.main_db
users_col = db.users
groups_col = db.groups
music_col = db.music


class DB:
    def __init__(self):
        self._client = client
        self._db = db
        self.users = users_col
        self.groups = groups_col
        self.music = music_col

    def save_user(self, chat_id):
        self.users.update_one({'user_id': chat_id},
                              {'$set': {'open_pm': True}},
                              upsert=True)

    def save_group(self, chat_id):
        self.groups.update_one({'chat_id': chat_id},
                               {'$set': {'chat_id': chat_id}},
                               upsert=True)

    def save_music(self, yt_id, file_id):
        self.music.update_one({'music': {'$exists': True}},
                              {'$set': {yt_id: file_id}},
                              upsert=True)

    def find_music(self, yt_id):
        result = self.music.find_one({yt_id: {'$exists': True}})
        if result:
            return result[yt_id]
