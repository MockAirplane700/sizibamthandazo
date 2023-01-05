from abc import ABC, abstractmethod


class StoriesDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_all_stories(self):
        return None

    @abstractmethod
    def add_new_story(self, story):
        pass

    @abstractmethod
    def update_story(self, story_id):
        pass
