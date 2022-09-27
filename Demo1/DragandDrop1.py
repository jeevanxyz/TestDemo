import time

import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://jqueryui.com/droppable/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame(By.XPATH,"//iframe[@class='demo-frame']")
source=driver.find_element(By.XPATH,"//div[@id='draggable']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")
act=ActionChains(driver)
act.drag_and_drop(source,target).perform()
time.sleep(3)
