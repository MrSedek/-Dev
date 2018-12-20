# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def open_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver, username, password):
        # login
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_group_page(self, driver):
        # open group page
        driver.find_element_by_link_text("groups").click()

    def create_new_group(self, driver, group):
        # create new group
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
        # return group test
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        driver = self.driver
        self.open_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_group_page(driver)
        self.create_new_group(driver, Group(name="NewGroup1", header="NewGroupHeader", footer="NewGroupFooter"))
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_group_page(driver)
        self.create_new_group(driver, Group(name="", header="", footer=""))
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
