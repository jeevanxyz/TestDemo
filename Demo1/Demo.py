from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Python Notes\Python Selenium\drivers\chromedriver.exe")
url="http://localhost/login.do"
driver.get(url)
#enter username
unTF=driver.find_element(By.XPATH,"//input[@id='username']")
unTF.send_keys("admin")
print("Text present inside the username text field is ",unTF.get_attribute("value"))
#enter password
pwdTF=driver.find_element(By.XPATH,"//input[@name='pwd']")
pwdTF.send_keys("manager")
AV=pwdTF.get_attribute("id")
print("Attribute value of id is ",AV)
loginbtn=driver.find_element(By.XPATH,"(//div[contains(text(),'Login ')])[1]")
#to check login button is enabled or not
if loginbtn.is_enabled():
    print("Button is enabled")
else:
    print("Button is not enabled")
keepmeloggedin=driver.find_element(By.XPATH,"//input[@id='keepLoggedInCheckBox']")
#to check keep me logged in check box is selected or not
if keepmeloggedin.is_selected():
    print("Check box is selected")
else:
    print("Check box is not selected")
#to check actitime logo is displayed or not
actitimelogo=driver.find_element(By.XPATH,"//img[@src='/img/default/login/timer.gif?hash=1106883454']")
if actitimelogo.is_displayed():
    print("Image is displayed")
else:
    print("Image not displayed")
# to get the text of an element
viewlicenselink=driver.find_element(By.XPATH,"//a[@id='licenseLink']")
print("Text of an element is",viewlicenselink.text)
# to get the tag of an element
tagofele=viewlicenselink.tag_name
print("Tag of element is",tagofele)
#location of an element
locationofele=actitimelogo.location
print(locationofele)
sizeofele=viewlicenselink.size
print("Size of the link",sizeofele)
color=unTF.value_of_css_property("color")
print(color)
fontsize=loginbtn.value_of_css_property('font-size')
print(fontsize)







