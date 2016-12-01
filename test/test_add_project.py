from model.project import Project

def test_add_project(app, db):
    old_list = app.soap.get_project_list()
    project = Project(name=app.project.random_string("name",10), description=app.project.random_string("description",20))
    #old_listprojects = db.get_project_list()
    app.project.create(project)
    #new_listprojects=db.get_project_list()
    #assert len(old_listprojects) +1 == len(new_listprojects)
    #old_listprojects.append(project)
    #assert sorted(old_listprojects ,key=Project.id_or_max) == sorted(new_listprojects ,key=Project.id_or_max)

    new_list = app.soap.get_project_list()
    old_list +=[project]
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
