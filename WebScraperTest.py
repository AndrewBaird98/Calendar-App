#import requests
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os,sys,inspect
import tkinter as tk
def FindEvents(outputBox):
    current_folder= os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))
    chromedriver = os.path.join(current_folder,"chromedriver.exe")

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get("https://www.sandiego.org/explore/events.aspx")
    soup = BeautifulSoup(driver.page_source,'lxml')
    #print(soup)
    for links in soup.find_all('div',class_="filters__results-list"):
        #print(links.get_text())
        outputBox.insert(tk.END, links.get_text())
    driver.close()
#print(result.status_code)
#src = result.content
#print(src)

#soup = BeautifulSoup(src, 'lxml')

#urls = []
#for div_tag in soup.find_all("div"):
   # urls.append(div_tag)
#for tag in urls:
   # print(tag)