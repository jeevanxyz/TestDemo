from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="http://localhost/login.do"
driver.get(url)
driver.maximize_window()
element=driver.find_element(By.ID,"licenseLink")
#getting the text of an element by using JS
eletext=driver.execute_script("return document.getElementById('licenseLink').textContent")
print(eletext)
#driver.execute_script("document.getElementById('licenseLink').click()")
time.sleep(2)
driver.execute_script("arguments[0].click()",element)
