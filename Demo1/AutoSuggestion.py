import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://www.google.com/?safe=active&ssui=on"
driver.get(url)
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys("Selenium")
time.sleep(1)
allSug=driver.find_elements(By.XPATH,"//span[text()='selenium']")
fifth_element=allSug[4]
fifth_element.click()
