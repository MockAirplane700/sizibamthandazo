from persistence.ars_corpia_persistence import CorpiaPersistence
from persistence.ars_corpia_persistence.fake_corpia_db import FakeCorpiaDB


class CorpiaSingleton:
    _instance = None

    def __init__(self):
        db = FakeCorpiaDB()
        self.db_interface = CorpiaPersistence(db)

    def __new__(cls, *args, **kwargs):
        if not CorpiaSingleton._instance:
            CorpiaSingleton._instance = object.__new__(cls)
        return CorpiaSingleton._instance

    def get_all_corpia(self):
        return self.db_interface.get_all_corpia()

    def add_new_coripa(self, corpia):
        return self.db_interface.add_new_corpia(corpia)

    def delete_corpia(self, corpia_id):
        return self.db_interface.delete_corpia(corpia_id)
