from persistence import ProjectsPersistence
from persistence.fake_projects_db import FakeProjectsDB


class ProjectsSingleton:
    _instance = None

    def __init__(self):
        db = FakeProjectsDB()
        self.db_interface = ProjectsPersistence(db)

    def __new__(cls, *args, **kwargs):
        if not ProjectsSingleton._instance:
            ProjectsSingleton._instance = object.__new__(cls)
        return ProjectsSingleton._instance

    def get_all_projects(self):
        return self.db_interface.get_all_projects()

    def add_new_project(self, project):
        return self.db_interface.add_new_project(project)

    def update_project(self, project_id):
        return self.db_interface.update_project(project_id)
