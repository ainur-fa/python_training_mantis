from suds.client import Client
from suds.client import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.3.4/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        list_projects=[]
        client = Client("http://localhost/mantisbt-1.3.4/api/soap/mantisconnect.php?wsdl")
        projects_list=client.service.mc_projects_get_user_accessible("administrator", "root")
        for project in projects_list:
            list_projects.append(Project(name=project.name, description=project.description, id=project.id))
        return list_projects
