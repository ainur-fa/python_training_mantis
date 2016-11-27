import pymysql.cursors
from model.project import Project

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host=host
        self.name=name
        self.user =user
        self.password=password
        self.connection=pymysql.connect(host=host, database=name, user=user,password=password)
        self.connection.autocommit(True)

    def get_project_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, description from mantis_project_table")
            for row in cursor:
                (id, name, description) = row
                list.append(Project(id=str(id), name=name, description=description))
        finally:
            cursor.close()
        return list


    def get_contact_fields(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 from addressbook where  deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    homephone=home, mobilephone=mobile, workphone=work,
                                    email=email, email2=email2, email3=email3, secondaryphone=phone2))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()