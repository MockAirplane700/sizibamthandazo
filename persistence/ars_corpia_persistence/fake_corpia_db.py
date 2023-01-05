from persistence.ars_corpia_persistence.corpia_database import CorpiaDatabase

coripae = {
    "corpiae": []
}


class FakeCorpiaDB(CorpiaDatabase):

    def __init__(self):
        self.db = None

    def connect_db(self):
        self.db = coripae

    def get_all_corpia(self):
        return coripae["corpia"]

    def add_new_corpia(self, corpia):
        coripae["corpiae"].append(corpia)
        return None

    def delete_corpia(self, corpia_id):
        return None
