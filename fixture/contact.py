import logging
from time import sleep
import re

from model.contact import Contact

LOGGER = logging.getLogger(__name__)


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        # driver.find_element_by_link_text("group").click()
        if not (driver.current_url.endswith("/addressbook/") or driver.current_url.endswith("index.php") and len(driver.find_elements_by_name("MainForm")) > 0):
            driver.find_element_by_link_text('Добавить контакт').click()

#    def return_to_home_page(self):
#        driver = self.app.driver
#        # return group test
#        driver.find_element_by_link_text('Добавить контакт').click()
#        # driver.find_element_by_link_text('group page').click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_contact_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                name = cells[2].text.split(' ')
                firstname = name[2]
                lastname = name[1]
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones=all_phones))
                print(self.contact_cache[0])
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        driver.get('http://localhost/addressbook/edit.php?id=' + str(index))

    def open_contact_to_view_by_index(self, index):
        driver = self.app.driver
        self.open_contact_page()
        driver.get('http://localhost/addressbook/view.php?id=' + str(index))

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_info_from_view_page(self,index):
        driver = self.app.driver
        self.open_contact_to_view_by_index(index)
        content = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", content).group(1)
        mobilephone = re.search("M: (.*)", content).group(1)
        workphone = re.search("W: (.*)", content).group(1)
        secondaryphone = re.search("P: (.*)", content).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def count(self):
        driver = self.app.driver
        self.open_contact_page()
        return len(driver.find_elements_by_name("selected[]"))
"""
    def fill_group_form(self, group):
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)
"""

