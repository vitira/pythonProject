from utilities import *
from selenium import webdriver
from time import *

# pick driver which will open webpage and make variable for it
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# tell driver wait untl everything download but not longer then 20 seconds
driver.implicitly_wait(20)

# maximize window
driver.maximize_window()

# open website "http://automationpractice.com/index.php"
url = "http://automationpractice.com/index.php"
driver.get(url)

# Save a screen shot of the website page
picture = f"./screenshots/{get_str_seconds()}practice.png"
driver.get_screenshot_as_file(picture)

# Find "Sign in" web element and click
driver.find_element_by_xpath('//a[@class="login"]').click()
sleep(5)

# Find email address text box web element
driver.find_element_by_xpath("//input[@id='email']").clear()

# Fill in email "123456abc@gmail.com"
driver.find_element_by_xpath("//input[@id='email']").send_keys('123456abc@gmail.com')

# Find password text box web element
driver.find_element_by_xpath("//input[@id='passwd']").clear()

# Fill in password "1234567"
driver.find_element_by_xpath("//input[@id='passwd']").send_keys("1234567")

# Find "Sign in" button and click
driver.find_element_by_xpath('//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/p[2]/button[1]/span[1]').click()
# # driver.quit()

sleep(5)
driver.close()

