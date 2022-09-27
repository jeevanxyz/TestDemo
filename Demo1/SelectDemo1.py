import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="file:///C:/Python%20Notes/Python%20Selenium/Sample%20Webpages/dropdown2.html"
driver.get(url)
countrydd=driver.find_element(By.XPATH,"//select[@name='Country']")
sel=Select(countrydd)
allOptions=sel.options
for option in allOptions:
    sel.select_by_visible_text(option.text)
    time.sleep(1)
sel.deselect_all()
sel.select_by_index(0)
sel.select_by_index(1)
selected_options=sel.all_selected_options
for option in selected_options:
    print(option.text)