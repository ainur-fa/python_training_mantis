import random
import string

from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app, db):
    project = Project(name=random_string("name", 10), description=random_string("description", 20))
    old_listprojects = db.get_project_list()
    app.project.create(project)
    new_listprojects=db.get_project_list()
    assert len(old_listprojects) +1 == len(new_listprojects)
    old_listprojects.append(project)
    assert sorted(old_listprojects ,key=Project.id_or_max) == sorted(new_listprojects ,key=Project.id_or_max)

