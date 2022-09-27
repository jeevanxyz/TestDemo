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
username=driver.find_element(By.XPATH,"//input[@id='username']")
password=driver.find_element(By.XPATH,"//input[@name='pwd']")
driver.execute_script("arguments[0].value='admin'",username)
driver.execute_script("arguments[0].value='manager'",password)
