class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        driver = self.app.driver
        # return group test
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.driver
        # create new group
        self.open()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()
        self.return_to_group_page()
