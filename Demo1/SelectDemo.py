import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="file:///C:/Python%20Notes/Python%20Selenium/Sample%20Webpages/dropdown1.html"
driver.get(url)
dropdown=driver.find_element(By.XPATH,"//select[@id='lang']")
sel=Select(dropdown)
sel.select_by_index(1)
time.sleep(1)
sel.select_by_value("golang")
time.sleep(1)
sel.select_by_visible_text("JavaScript")
time.sleep(1)
if sel.is_multiple:
    print("it is a multiselect dd")
else:
    print("it is a single select dd")
allOptions=sel.options
print("The no of options present in the dd is",len(allOptions))
for option in allOptions:
    print(option.text)
