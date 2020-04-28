from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get('https://accounts.zoho.com/signin?servicename=ZohoChat&signupurl=https://www.zoho.com/cliq/signup.html')
driver.find_element_by_id('login_id').send_keys('himanshu19@navgurukul.org')
driver.find_element_by_id('nextbtn').submit()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="password"]').send_keys('vklm1810')
driver.find_element_by_xpath('//*[@id="nextbtn"]').click()
time.sleep(30)
search = driver.find_element_by_xpath('//*[@id="GS-search-field"]')
time.sleep(2)
search.send_keys('mohit')
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)
message = driver.find_element_by_id('composer2243191776009849574')
message.send_keys('hello mr. IT')
message.send_keys(Keys.ENTER)

