import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        # driver.find_element_by_xpath("css=input[type='submit']").click()
        driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@id='top']/form/a").click()
        time.sleep(1)
