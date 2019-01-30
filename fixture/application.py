from selenium import webdriver
# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
# from fixture.new_user import NewUserHelper


class Application:

    def __init__(self, browser, base_url):
#        self.driver = WebDriver(executable_path=r'd:/~Sedek/WebDrivers/chromedriver.exe',
#                                chrome_binary=r'"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"')
        if browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=r'd:/~Sedek/WebDrivers/geckodriver.exe',
                                firefox_binary=r'c:/Program Files/Mozilla Firefox/firefox.exe')
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Неопределен браузер %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
#        self.new_user = NewUserHelper(self)

    def open_page(self):
        driver = self.driver
        driver.get(self.base_url)
        assert "Адресная книга" in driver.title

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False