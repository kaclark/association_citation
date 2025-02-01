import requests

from bs4 import BeautifulSoup
from pprint import pprint

from urllib.parse import urljoin
import webbrowser

import re

from selenium import webdriver

def soup_scrape():
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
              }
    page = requests.get("https://twitter.com/nonmarkov_field", headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.get_text())

def selenium_scrape():
    browser = webdriver.Firefox()
    browser.get("https://twitter.com/nonmarkov_field")

selenium_scrape()
