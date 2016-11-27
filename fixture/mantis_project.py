# -*- coding: utf-8 -*-
from model.project import Project
import random
import string

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input.button-small").click()
        self.fill_project_form("project-name", project.name)
        self.fill_project_form("project-description", project.description)
        wd.find_element_by_xpath("//span[@class='submit-button']/input").click()
        wd.find_element_by_link_text("Proceed").click()

    def delete(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/div/form/input[4]").click()


    def fill_project_form(self, field, text):
        wd = self.app.wd
        wd.find_element_by_id(field).click()
        wd.find_element_by_id(field).clear()
        wd.find_element_by_id(field).send_keys(text)