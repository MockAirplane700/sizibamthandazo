from abc import ABC, abstractmethod


class ProjectsDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_all_projects(self):
        return None

    @abstractmethod
    def add_new_project(self, project):
        pass

    @abstractmethod
    def update_project(self, projectId):
        pass
