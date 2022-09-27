from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")

driver=webdriver.Chrome(service=driver_service)
url="http://localhost/login.do"
driver.get(url)
#enter username
username=driver.find_element(By.XPATH,"//input[@id='username']")
username.send_keys("admin")
#select the value present in username field
username.send_keys(Keys.CONTROL+'a')
#copy the value
username.send_keys(Keys.CONTROL+'c')
#paste the value to the password field
password=driver.find_element(By.XPATH,"//input[@name='pwd']")
password.send_keys(Keys.CONTROL+'v')
password.send_keys(Keys.CONTROL+'a')
password.send_keys(Keys.DELETE)
password.send_keys("manager")
ViewLicense=driver.find_element(By.XPATH,"//a[@id='licenseLink']")
#ViewLicense.send_keys(Keys.CONTROL+Keys.ENTER)
#ViewLicense.send_keys(Keys.SHIFT+Keys.ENTER)
loginbtn=driver.find_element(By.XPATH,"//a[@id='loginButton']")
loginbtn.send_keys(Keys.ENTER)

