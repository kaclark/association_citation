######
#Markdown
#####
#```bash
#python webgtk-selenium.py 'https://en.wikipedia.org/wiki/Proclus'
#```

import sys
from selenium import webdriver

options = webdriver.WebKitGTKOptions()
driver = webdriver.WebKitGTK(options=options)
driver.get(sys.argv[1])
