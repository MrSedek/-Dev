import os

import selenium
from selenium.webdriver.android import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
print(gecko+'.exe')
driver = webdriver.Firefox()
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
browser = selenium.webdriver.Firefox(firefox_binary=binary,executable_path=gecko+'.exe')
browser = webdriver.Firefox(executable_path="C:\~Drivers\geckodriver.exe")
browser.get('http:///www.google.com')
browser.close()