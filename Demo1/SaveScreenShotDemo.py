

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="http://localhost/login.do"
driver.get(url)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@name='pwd']").send_keys("manager")
driver.get_screenshot_as_file("C:\\Python Notes\\Python Selenium\\Sample Webpages\\Sample.png")