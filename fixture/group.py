class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        # driver.find_element_by_link_text("group").click()
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

    def select_first_group(self):
        driver = self.app.driver
        # select first group
        # driver.find_element_by_xpath('//*[@id="content"]/form/input[4]').click()
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # open modification form
        # submit modification
        driver.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        driver.find_element_by_name("update").click()
        self.return_to_group_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_group_page()
