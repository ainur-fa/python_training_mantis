from model.project import Project
import random

def test_del_project(app, db):

    if len(db.get_project_list()) == 0:
        project = Project(name=app.project.random_string("name", 10),
                          description=app.project.random_string("description", 20))
        app.project.create(project)

    old_list = app.soap.get_project_list()
    old_listprojects = db.get_project_list()
    for_delete_project = random.choice(old_listprojects)
    app.project.delete(for_delete_project)
    #new_listprojects = db.get_project_list()
    #old_listprojects.remove(for_delete_project)
    #assert new_listprojects == old_listprojects
    new_list = app.soap.get_project_list()
    #old_list.remove(for_delete_project)
    old_list= [elem for elem in old_list if str(elem) != str(for_delete_project)]
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
