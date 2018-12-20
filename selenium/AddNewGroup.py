# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def open_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver):
        # login
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_group_page(self, driver):
        # open group page
        driver.find_element_by_link_text("groups").click()

    def create_new_group(self, driver):
        # create new group
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("NewGroup1")
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("NewGroupHeader")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("NewGroupFooter")
        driver.find_element_by_name("submit").click()
        # return group test
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_page(driver)
        self.login(driver)
        self.open_group_page(driver)
        self.create_new_group(driver)
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
