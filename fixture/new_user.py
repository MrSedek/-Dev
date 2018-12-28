from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

"""
class NewUserHelper:
    def __init__(self, app):
        self.app = app

    def open(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        driver = self.app.driver
        # return group test
        driver.find_element_by_link_text("home page").click()

    def create(self, new_user):
        driver = self.app.driver
        # create new group
        self.open()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(new_user.fName)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(new_user.mName)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(new_user.lName)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(new_user.nickName)
        driver.find_element_by_name("photo").click()
        driver.find_element_by_name("photo").clear()
        driver.find_element_by_name("photo").send_keys("C:\\fakepath\\0cb40312-3390-415a-8000-eb9d0667ce6c.jpg")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(new_user.title)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(new_user.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(new_user.address)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(new_user.hTel)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(new_user.mTel)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(new_user.wTel)
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(new_user.fTel)
        driver.find_element_by_name("email").send_keys(Keys.DOWN)
        driver.find_element_by_name("email").send_keys(Keys.DOWN)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(new_user.eMail)
        driver.find_element_by_name("email").send_keys(Keys.DOWN)
        driver.find_element_by_name("email").send_keys(Keys.TAB)
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(new_user.localhost)
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(new_user.sAddress)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(new_user.sHome)
        driver.find_element_by_name("phone2").send_keys(Keys.DOWN)
        driver.find_element_by_name("phone2").send_keys(Keys.TAB)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.return_to_home_page()
        
"""