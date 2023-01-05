from persistence.ars_corpia_persistence.artist_database import ArtistDatabase

artists = {
    "artists": [{
        'id' : 0,
        'name' : 'John die'
    }]
}


class FakeArtistsDB(ArtistDatabase):
    def __init__(self):
        self.db = None

    def connect_db(self):
        self.db = artists

    def get_all_artists(self):
        return artists["artists"]

    def add_new_artist(self, artist):
        artists["artists"].append(artist)
        return None

    def delete_artist(self, artist_id):
        return None
