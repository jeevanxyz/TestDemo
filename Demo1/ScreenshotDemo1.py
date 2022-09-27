from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://nxtgenaiacademy.com/alertandpopup/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
alertbox=driver.find_element(By.XPATH,"//button[@name='confirmalertbox']")
alertbox.click()
pyautogui.screenshot().save("Sample2.png")