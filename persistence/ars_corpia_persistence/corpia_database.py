from abc import ABC, abstractmethod


class CorpiaDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_all_corpia(self):
        return None

    @abstractmethod
    def add_new_corpia(self, corpia):
        pass

    @abstractmethod
    def delete_corpia(self, corpia_id):
        pass
