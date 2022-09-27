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
allOptions=sel.options
all_text=[]
for option in allOptions:
    value=option.text
    all_text.append(value)
text=all_text.sort(reverse=True)
for text in all_text:
    print(text)
