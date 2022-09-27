from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://www.youtube.com/watch?v=gT9qnZi3f74"
driver.get(url)
driver.maximize_window()
time.sleep(3)
#driver.execute_script("alert('Welcome to Qspiders')")
title=driver.execute_script("return document.title")
url=driver.execute_script("return document.URL")
domain=driver.execute_script("return document.domain")
print(title)
print(url)
print(domain)