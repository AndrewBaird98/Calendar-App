#import requests
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os,sys,inspect
import tkinter as tk
import time
from Event import Event
def FindEvents(outputBox):
    current_folder= os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))
    chromedriver = os.path.join(current_folder,"chromedriver.exe")

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get("https://www.sandiego.org/explore/events.aspx")
    driver.find_element_by_xpath('//button[@class="submit-button__secondary load-more"]').click()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source,'lxml')
    #print(soup)
    eventlist = []
    for links in soup.find_all('section',class_="result"):
        E = Event(links.find('a',class_="result__title-link").get_text(),links.find('div',class_="result__dates").get_text(),
                  "Not Know","Not Known","Not Known","Not Known","Not Known", links.find('div',class_="result__tag").get_text(),
                  "Not Know",links.find('a',class_="result__cta-link").get('href'),"Not Known")
        price = links.find('div',class_="result__price")
        if price:
            E.price=price.get_text()
        E.displayExample()
        #print(links.find('div',class_="result__tag").get_text())
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