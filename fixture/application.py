from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper
# from fixture.new_user import NewUserHelper


class Application:

    def __init__(self):
        self.driver = WebDriver(executable_path=r'd:/~Sedek/WebDrivers/geckodriver.exe',
                                firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
#        self.driver = WebDriver(executable_path=r'd:/~Sedek/WebDrivers/chromedriver.exe',
#                                chrome_binary=r'"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"')
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
#        self.new_user = NewUserHelper(self)

    def open_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        assert "Адресная книга" in driver.title

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False