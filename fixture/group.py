import logging
from model.group import Group

LOGGER = logging.getLogger(__name__)


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        # driver.find_element_by_link_text("group").click()
        if not (driver.current_url.endswith("/groups.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_link_text('Группы').click()

    def return_to_group_page(self):
        driver = self.app.driver
        # return group test
        driver.find_element_by_link_text('Группы').click()
        # driver.find_element_by_link_text('group page').click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)

    def create(self, group):
        driver = self.app.driver
        # create new group
        self.open_group_page()
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        # driver.find_element_by_name('submit').click()
        driver.find_element_by_xpath('//input[@name="submit"]').click()
        self.return_to_group_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification form
        # submit modification
        driver.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        driver.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_group_page()
            self.group_cache = []
            print(driver.find_elements_by_xpath("//input[@name='selected[]']"))

            for element in driver.find_elements_by_xpath("//input[@name='selected[]']"):
                title_element = element.get_attribute("title") [8:-1]
                id = element.get_attribute("value")
                self.group_cache.append(Group(name = title_element, id = id))
        return list(self.group_cache)

        