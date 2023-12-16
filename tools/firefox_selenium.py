from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import sys

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get(sys.argv[1])
driver.implicitly_wait(10)
tweet_info = driver.find_element(By.CLASS_NAME, "css-175oi2r").text
print(tweet_info)
driver.quit()
