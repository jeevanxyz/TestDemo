from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui

driver_service = Service(executable_path="C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get(
    "https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_6vkm4swd5x_b&adgrpid=60611463244&hvpone=&hvptwo=&hvadid=617724335923&hvpos=&hvnetw=g&hvrand=9954010243321123690&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062064&hvtargid=kwd-320833120261&hydadcr=15413_2322997&gclid=EAIaIQobChMI0LfovOqz-gIVCZNmAh1fmQa7EAAYASAAEgKKy_D_BwE")
driver.maximize_window()
time.sleep(3)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
# to scrolldown to a specific element
homedecor = driver.find_element(By.XPATH, "//span[text()='Up to 60% off | Home décor picks from local shops']")
driver.execute_script("arguments[0].scrollIntoView();", homedecor)
