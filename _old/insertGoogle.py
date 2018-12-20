# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("insert text")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.close()

if __name__ == "__main__":
    unittest.main()
