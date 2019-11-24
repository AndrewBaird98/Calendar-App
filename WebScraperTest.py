#import requests
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os,sys,inspect
import tkinter as tk
import time
from Event import Event
from selenium.common.exceptions import NoSuchElementException
import PySide2
def FindEvents(outputBox):
    current_folder= os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))
    chromedriver = os.path.join(current_folder,"chromedriver")

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get("https://www.sandiego.org/explore/events.aspx")
    driver.find_element_by_xpath('//button[@class="submit-button__secondary load-more"]').click()
    time.sleep(0.1)
    soup = BeautifulSoup(driver.page_source,'lxml')
    #print(soup)
    eventlist = []
    for links in soup.find_all('section',class_="result"):
        #print(links.find('div', class_="result__tag").get_text())
        E = Event(links.find('a',class_="result__title-link").get_text(),links.find('div',class_="result__dates").get_text(),
                  "Not Know","Not Known","Not Known","Not Known","Not Known", links.find('div',class_="result__tag").get_text(),
                  "Not Know",links.find('a',class_="result__cta-link").get('href'),"Not Known", "Not Known", "Not Known", "Not Known")

        outputBox.append(links.get_text())
        #E.displayExample()


    driver.close()
def EventInfoGrab(Einfo,popup):
    current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
    chromedriver = os.path.join(current_folder, "chromedriver")
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get(Einfo.link)
    extraBlocks = driver.find_elements_by_class_name('extra-block')
    extraBlocks.pop(0)
    try:
        FirstCheck = extraBlocks[0]
        Testing = FirstCheck.find_element_by_class_name('tag')
    except NoSuchElementException:
        print(FirstCheck.text)
        popup.setTest(FirstCheck.text)
        extraBlocks.pop(0)
        pass

    for found in extraBlocks:
        h3text = found.find_element_by_class_name('tag')
        Comparetext = h3text.text
        if Comparetext == 'Date & Time':
            FoundP = found.find_element_by_tag_name('p')
            clearstring = FoundP.text
            clearstring = clearstring.replace('\n', ' ')
            print(clearstring)
            popup.setInformativeText(clearstring)
    ShowMore = driver.find_element_by_xpath('//div[@class="links"]').click()
    time.sleep(1)
    try:
        EventDescription = driver.find_element_by_class_name('header-component__content')
        print(EventDescription.text)
        popup.setInformativeText(EventDescription.text)
        # NextDescription = driver.find_element_by_class_name('hidden body-style')
        # print(NextDescription.text)
    except NoSuchElementException:
        print("No Description found")
        popup.setTest("No Description found")
    driver.close()
#print(result.status_code)
#src = result.content
#print(src)

#soup = BeautifulSoup(src, 'lxml')

#urls = []
#for div_tag in soup.find_all("div"):
   # urls.append(div_tag)
#for tag in urls:
