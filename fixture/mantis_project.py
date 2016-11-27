# -*- coding: utf-8 -*-
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

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

    def fill_project_form(self, field, text):
        wd = self.app.wd
        wd.find_element_by_id(field).click()
        wd.find_element_by_id(field).clear()
        wd.find_element_by_id(field).send_keys(text)