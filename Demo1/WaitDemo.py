from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")

driver=webdriver.Chrome(service=driver_service)
url="http://localhost/login.do"
driver.get(url)
print(driver.title)
wait=WebDriverWait(driver,30)
status=wait.until(EC.title_is("actiTIME - Login"),"Verifying the tilte")
print(status)
username=driver.find_element(By.XPATH,"//input[@id='username']")
username.send_keys("admin")
password=driver.find_element(By.XPATH,"//input[@name='pwd']")
password.send_keys("manager")
loginbtn=driver.find_element(By.XPATH,"//a[@id='loginButton']")
loginbtn.send_keys(Keys.ENTER)



