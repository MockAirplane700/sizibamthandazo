class ProjectsPersistence:
    def __init__(self , projects_db):
        self._db = projects_db

    def get_all_projects(self):
        return self._db.get_all_projects()

    def add_new_project(self, project):
        return self._db.add_new_project(project)

    def update_project(self, project_id):
        return self._db.update_project(project_id)


class StoriesPersistence:
    def __init__(self, stories_db):
        self._db = stories_db

    def get_all_stories(self):
        return self._db.get_all_stories()

    def add_new_story(self, story):
        return self._db.add_new_story(story)

    def update_story(self, story_id):
        return self._db.update_story(story_id)