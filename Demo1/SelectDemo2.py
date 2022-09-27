from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

found=False
search_item=input("Enter the value to be searched")
driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="file:///C:/Python%20Notes/Python%20Selenium/Sample%20Webpages/dropdown1.html"
driver.get(url)
dropdown=driver.find_element(By.XPATH,"//select[@id='lang']")
sel=Select(dropdown)
all_Options=sel.options
for option in all_Options:
    value=option.text
    if value==search_item:
        found=True
        break
if found:
    print(search_item +" Found")
else:
    print(search_item +" Not Found")