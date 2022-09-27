import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
url="file:///C:/Python%20Notes/Python%20Selenium/Sample%20Webpages/Signup.html"
driver.get(url)
#entering value in first name
driver.find_element(By.XPATH,'/html/body/center/input[1]').send_keys("admin")
#entering value in last name
pwdTF=driver.find_element(By.XPATH,'/html/body/center/input[2]')
pwdTF.send_keys("manager")
time.sleep(1)
pwdTF.clear()

