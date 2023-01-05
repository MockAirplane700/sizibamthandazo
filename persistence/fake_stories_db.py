from persistence.stories_database import StoriesDatabase

stories = {
    "stories": [
        {
            "id": 0,
            "title": "some story",
            "summary": "lorem ipsum"
        }
    ]
}


class FakeStoriesDB(StoriesDatabase):
    def __init__(self):
        self.db = None

    def connect_db(self):
        self.db = stories

    def get_all_stories(self):
        return stories["stories"]

    def add_new_story(self, story):
        stories["stories"].append(story)

    def update_story(self, story_id):
        pass
