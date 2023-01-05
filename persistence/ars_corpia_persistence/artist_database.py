from abc import ABC, abstractmethod


class ArtistDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_all_artists(self):
        return None

    @abstractmethod
    def add_new_artist(self, artist):
        pass

    @abstractmethod
    def delete_artist(self, artist_id):
        pass
