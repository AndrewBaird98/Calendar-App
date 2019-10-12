#import requests
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#result = requests.get("https://www.google.com/search?rlz=1C1CHBD_enUS847US847&biw=958&bih=959&ei=062eXb3zLrKv0PEPrsOU-AM&q=concerts&oq=concerts&gs_l=psy-ab.3..0l10.32579.35048..35459...0.1..0.142.806.8j1......0....1..gws-wiz.....6..0i71j0i362i308i154i357j0i273j0i131j0i67.h-o3ZcasFBs&uact=5&ibp=htl;events&rciv=evn#fpstate=tldetail&htidocid=_-SGMC1iCVoU4VvkJpA8-A%3D%3D&htivrt=events")

import time
chromedriver= "/workspace/untitled1/driver/chromedriver"
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(chromedriver, options=options)
driver.get("https://www.google.com/")
soup = BeautifulSoup(driver.page_source,'lxml')
for links in soup.find_all('a'):
    print(links.get('href'),links.get_text())
#print(result.status_code)
#src = result.content
#print(src)

#soup = BeautifulSoup(src, 'lxml')

#urls = []
#for div_tag in soup.find_all("div"):
   # urls.append(div_tag)
#for tag in urls:
   # print(tag)