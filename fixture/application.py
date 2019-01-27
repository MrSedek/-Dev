from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper
# from fixture.new_user import NewUserHelper


class Application:

    def __init__(self):
        self.driver = WebDriver(executable_path=r'c:/~Develop/DriverPython/geckodriver.exe',
                                firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
#        self.new_user = NewUserHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
