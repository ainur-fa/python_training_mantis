from model.project import Project


def test_del_project(app, db):
    project_list = db.get_project_list()
    if project_list is None:
        app.project.create(project)