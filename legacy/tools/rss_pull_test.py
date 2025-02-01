import lxml
from bs4 import BeautifulSoup
import requests

import feedparser

leibniz_rss = "https://www.htmlcommentbox.com/rss_clean?page=https%3A%2F%2Fkaclark.github.io%2Fassociation_citation%2Flivescans%2Fleibniz_discourse_on_the_natural_theology_of_the_chinese.html&opts=16798&mod=$1$wq1rdBcg$nBJdQnVHQsOLpZa.oWVVU/"

leibniz_html = "https://kaclark.github.io/association_citation/livescans/leibniz_discourse_on_the_natural_theology_of_the_chinese.html"

def bsoup_html():
    rss_link = requests.get(leibniz_html)
    c_data = BeautifulSoup(rss_link.content, "html5lib")
    print(c_data.prettify())
    #c_data = BeautifulSoup(rss_link.content, "lxml")
    #for anchor in c_data.find_all('description'):
    #    print(anchor)

def bsoup_xml():
    rss_link = requests.get(leibniz_rss)
    c_data = BeautifulSoup(rss_link.content, "xml")
    print(c_data.prettify())
    #c_data = BeautifulSoup(rss_link.content, "lxml")
    #for anchor in c_data.find_all('description'):
    #    print(anchor)

def feed_parse():
    feed = feedparser.parse(leibniz_rss)
    print(feed)

#bsoup_xml()
#bsoup_html()
#feed_parse()
