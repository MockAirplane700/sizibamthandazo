import json


class ArtistPersistence:
    def __init__(self, artist_db):
        self._db = artist_db

    def get_all_artists(self):
        return self._db.get_all_artists()

    def add_new_artist(self, artist):
        return self._db.add_new_artist(artist)

    def delete_artist(self, artist_id):
        return self._db.delete_artist(artist_id)


class CorpiaPersistence:
    def __init__(self, corpia_db):
        self._db = corpia_db

    def get_all_corpia(self):
        return self._db.get_all_coripa()

    def add_new_corpia(self, coripa):
        return self._db.add_new_corpia(coripa)

    def delete_corpia(self, corpia_id):
        return self._db.delete_corpia(corpia_id)
