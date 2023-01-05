from persistence.projects_database import ProjectsDatabase

projects = {
    "projects": [
        {
            "id": 0,
            "title": "Project Artemis",
            "description": "lorem ipsum"
        }
    ],
}


class FakeProjectsDB(ProjectsDatabase):
    def __init__(self):
        self.db = None

    def connect_db(self):
        self.db = projects

    def get_all_projects(self):
        return projects["projects"]

    def add_new_project(self, project):
        projects["projects"].append(project)

    def update_project(self, projectId):
        pass
