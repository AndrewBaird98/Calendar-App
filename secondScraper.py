from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import os,sys,inspect
import tkinter as tk
import time
from Event import Event



current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
chromedriver = os.path.join(current_folder, "chromedriver")
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chromedriver, options=options)
driver.get("https://www.sandiego.org/explore/events/dining-and-nightlife/san-diego-bay-wine-and-food-festival.aspx")
extraBlocks=driver.find_elements_by_class_name('extra-block')
extraBlocks.pop(0)
try:
    FirstCheck = extraBlocks[0]
    Testing=FirstCheck.find_element_by_class_name('tag')
except NoSuchElementException:
    print(FirstCheck.text)
    extraBlocks.pop(0)
    pass

for found in extraBlocks:
    h3text = found.find_element_by_class_name('tag')
    Comparetext = h3text.text
    if Comparetext == 'Date & Time':
        FoundP=found.find_element_by_tag_name('p')
        clearstring = FoundP.text
        clearstring= clearstring.replace('\n',' ')
        print(clearstring)
ShowMore = driver.find_element_by_xpath('//div[@class="links"]').click()
time.sleep(1)
try:
    EventDescription = driver.find_element_by_class_name('header-component__content')
    print(EventDescription.text)
    #NextDescription = driver.find_element_by_class_name('hidden body-style')
    #print(NextDescription.text)
except NoSuchElementException:
    print("No Description found")
driver.close()

