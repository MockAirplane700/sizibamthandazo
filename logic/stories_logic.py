from persistence import StoriesPersistence
from persistence.fake_stories_db import FakeStoriesDB


class StoriesSingleton:
    _instance = None

    def __init__(self):
        db = FakeStoriesDB()
        self.db_interface = StoriesPersistence(db)

    def __new__(cls, *args, **kwargs):
        if not StoriesSingleton._instance:
            StoriesSingleton._instance = object.__new__(cls)
        return StoriesSingleton._instance

    def get_all_stories(self):
        return self.db_interface.get_all_stories()

    def add_new_story(self, story):
        return self.db_interface.add_new_story(story)

    def update_story(self, story_id):
        return self.db_interface.update_story(story_id)
