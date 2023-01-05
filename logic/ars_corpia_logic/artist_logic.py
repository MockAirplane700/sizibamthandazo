from persistence.ars_corpia_persistence import ArtistPersistence
from persistence.ars_corpia_persistence.fake_artist_db import FakeArtistsDB


class ArtistSingleton:
    _instance = None

    def __init__(self):
        db = FakeArtistsDB()
        self.db_interface = ArtistPersistence(db)

    def __new__(cls, *args, **kwargs):
        if not ArtistSingleton._instance:
            ArtistSingleton._instance = object.__new__(cls)
        return ArtistSingleton._instance

    def get_all_artists(self):
        return self.db_interface.get_all_artists()

    def add_new_artist(self, artist):
        return self.db_interface.add_new_artist(artist)

    def delete_artist(self, artist_id):
        return self.db_interface.delete_artist(artist_id)
