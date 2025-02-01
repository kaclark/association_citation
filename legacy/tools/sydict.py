import requests

from bs4 import BeautifulSoup
#from requests_html import HTMLSession
import requests
from pprint import pprint

from urllib.parse import urljoin
import webbrowser
import sys

import re

def format_search_res(s_url):
    search_results = []
    #search_set = ["French", "Eastern Syriac","phonetic", "English", "Category"]
    search_set = ["Eastern Syriac","phonetic", "English", "Category"]
    dterm = "Dialect"
    page = requests.get(s_url)
    soup = BeautifulSoup(page.content, "html.parser")
    for trow in soup.find_all("tr"):
        if dterm in trow.get_text():
            continue
        dtrow = []
        for sterm in search_set:
            if sterm in trow.get_text():
                for td in trow.find_all("td"):
                    if sterm == "phonetic":
                        if "phonetic" not in td.get_text():
                            dtrow.append("phonetic")
                            dtrow.append("".join(td.get_text().split(' ')))
                    else: 
                        dtrow.append(td.get_text())
            try:
                if sterm in dtrow[0]: 
                    search_results.append(" ".join(dtrow) + "\n" + "-"*30)
            except IndexError:
                pass
    print("\n".join(search_results))
    print('\n')
    nxt = input("[press ENTER for next result]")
    print("\n")

def search():
    url = "https://www.lexilogos.com/english/syriac_dictionary.htm"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    forms = soup.find_all("form")
    for form in forms: 
        details = {}
        action = form.attrs.get("action").lower()
        method = form.attrs.get("method", "get").lower()
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value =input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": input_name, "value": input_value})
        for select in form.find_all("select"):
            select_name = select.attrs.get("name")
            select_type = "select"
            select_options = []
            select_default_value = ""
            for select_option in select.find_all("option"):
                option_value = select_option.attrs.get("value")
                if option_value:
                    select_options.append(option_value)
                    if select_option.attrs.get("selected"):
                        select_default_value = option_value
            if not select_default_value and select_options:
                select_default_value = select_options[0]
                inputs.append({"type": select_type, "name": select_name, "values": select_options, "value": select_default_value})
        for textarea in form.find_all("textarea"):
            textarea_name = textarea.attrs.get("name")
            textarea_type = "textarea"
            textarea_value = textarea.attrs.get("value", "")
            inputs.append({"type": textarea_type, "name": textarea_name, "value": textarea_value})
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        n_url = urljoin(url, details["action"])
        data = {}
        for input_tag in details["inputs"]:
            if input_tag["type"] == "hidden":
                data[input_tag["name"]] = input_tag["value"]
            elif input_tag["type"] == "select":
                for i, option in enumerate(input_tag["values"], start=1):
                    if option == input_tag["value"]:
                        print(f"{i} # {option} (default)")
                    else:
                        print(f"{i} # {option}")
                choice = input(f"Enter the option for the select field '{input_tag['name']}' (1-{i}): ")
                try:
                    choice = int(choice)
                except:
                    value = input_tag["value"]
                else:
                    value = input_tag["values"][choice-1]
                data[input_tag["name"]] = value
            elif input_tag["type"] != "submit":
                value = input(f"English Search Term: ")
                data[input_tag["name"]] = value
        headers = {
  'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,ar;q=0.6',                                                    'user-agent': 'Firefox'                                                } 
        res = requests.post(n_url, headers=headers, data=data)
        soup = BeautifulSoup(res.content, "html.parser")
        url_prefix = "http://www.assyrianlanguages.org/sureth/"
        for li in soup.find_all('li'):
            redirect = url_prefix + li.find('a')['href']
            if "main menu" not in li.get_text() and "Perform another" not in li.get_text():
                try:
                    format_search_res(redirect)
                except ValueError:
                    pass

e_or_s = input("English Search[e]\nSyriac Search[s]\nChoice: ")
if e_or_s == 'e':
    search()
elif e_or_s == 's':
    url_prefix_sy = "http://www.google.com/search?q=" 
    syterm = input("Syriac Search Term: ")
    headers = {
  'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,ar;q=0.6',
  'user-agent': 'Firefox'
              }
    page = requests.get(url_prefix_sy + syterm, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    potential_sinks = []
    for searchres in soup.find_all('a'):
        slink = searchres['href']
        if "sureth" in slink and "id" in slink:
            format_search_res(slink)

