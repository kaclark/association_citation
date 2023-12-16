from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import time

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
res = driver.get("http://google.com/")
print ("Headless Firefox Initialized")
driver.quit()
