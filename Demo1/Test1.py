from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")

driver=webdriver.Chrome(service=driver_service)
url="http://localhost/login.do"
driver.get(url)
elements=driver.find_elements(By.XPATH,"//a")
print("The number of links present in actitime page",len(elements))
for ele in elements:
    url=ele.get_attribute("href")
    print(url)

images=driver.find_elements(By.XPATH,'//img')
print("Number of images preent in actitime webpage is ",len(images))