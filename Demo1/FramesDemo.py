from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://docs.seleniumhq.org/"
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,"//span[.='Downloads']").click()
driver.find_element(By.XPATH,"(//a[.='API Docs'])[3]").click()
time.sleep(2)
#driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"(//a[text()='Frames'])[1]").click()
