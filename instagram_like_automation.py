from selenium import webdriver
from contextlib import contextmanager
import time
import sys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/accounts/login/")

# During 1 minute, system will be waited for user to log in and click not now js or user will be extracted following comment lines.
time.sleep(60)

#notnow = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]")
#notnow.click()
#time.sleep(5)

a = 1
# System will be work about 10 hours and like 7000 times.
while a < 1000: 
	browser.get("https://www.instagram.com/")
	time.sleep(6)
	# Just first 7 photos have regular xpaths. So refresh is required. 
	b = 1
	while b < 8:
		first_pic = browser.find_element_by_xpath("/html/body/span/section/main/section/div[1]/div[1]/div/article["+str(b)+"]/div[2]/section[1]/span[1]/button/span")
		first_pic.click()		
		time.sleep(2)
		b = b+1
		time.sleep(2)
	a = a+1
	

