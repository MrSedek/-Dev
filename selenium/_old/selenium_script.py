import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\~Drivers\geckodriver.exe")
time.sleep(5)
driver.quit()