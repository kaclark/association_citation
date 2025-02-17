######
#Markdown
#####
#```bash
#python webgtk-selenium.py 'https://en.wikipedia.org/wiki/Proclus'
#```

import sys
from selenium import webdriver

options = webdriver.WebKitGTKOptions()
#options.add_argument('--headless')
driver = webdriver.WebKitGTK(options=options)
#driver.get(sys.argv[1])
driver.get("https://www.duckduckgo.com")
print(driver.page_source)
driver.close()
