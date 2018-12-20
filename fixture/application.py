from  selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = WebDriver();
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        driver = self.driver
        # return group test
        driver.find_element_by_link_text("group page").click()

    def create_new_group(self, group):
        driver = self.driver
        # create new group
        self.open_group_page()
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

    def destroy(self):
        self.driver.quit()
