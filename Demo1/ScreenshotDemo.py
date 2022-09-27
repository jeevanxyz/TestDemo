from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service=Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=driver_service)
url="https://www.google.com/?safe=active&ssui=on"
driver.get(url)
element=driver.find_element(By.XPATH,"//img[@alt='Google']")
location=element.location
size=element.size
driver.save_screenshot('Google.png')
x=location['x']
y=location['y']
width=location['x']+size['width']
height=location['y']+size['height']
im=Image.open('Google.png')
im=im.crop((int(x),int(y),int(width),int(height)))
im.save('Cropped_image.png')
