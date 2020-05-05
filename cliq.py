from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
username= input("ENTER YOUR CLIQ USER NAME OR GAMIL     ")
password= input("ENTER YOUR CLIQ PASSWORD      ")
search_name = input(" 	 ENTER THE NAME OF THE PERSON YOU WANT TO search")
message_to_user = input("  ENTER THE message YOU WANT TO SEND TO searched user")

driver=webdriver.Chrome()
driver.get('https://accounts.zoho.com/signin?servicename=ZohoChat&signupurl=https://www.zoho.com/cliq/signup.html')
driver.find_element_by_id('login_id').send_keys(username)
driver.find_element_by_id('nextbtn').submit()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="nextbtn"]').click()
time.sleep(30)
search = driver.find_element_by_xpath('//*[@id="GS-search-field"]')
time.sleep(2)
search.send_keys(search_name)
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)
message = driver.find_element_by_id('composer2243191776009849574')
message.send_keys(message_to_user)
message.send_keys(Keys.ENTER)

