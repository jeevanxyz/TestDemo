import time

import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://www.actimind.com/"
driver.get(url)
time.sleep(2)
abtcompany=driver.find_element(By.XPATH,"//a[contains(text(),'ABOUT')]")
act=ActionChains(driver)
time.sleep(1)
#act.context_click(abtcompany).send_keys(Keys.CONTROL+Keys.ENTER).perform()
#keyboard.press('t')
#keyboard.press('w')
act.context_click(abtcompany.send_keys(Keys.SHIFT+Keys.ENTER)).perform()



