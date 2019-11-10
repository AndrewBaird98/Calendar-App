from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
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
driver.get("https://www.sandiego.org/explore/events/festivals-and-street-fairs/la-jolla-concours-delegance.aspx")
extraBlocks=driver.find_elements_by_class_name('extra-block')
extraBlocks.pop(0)

for found in extraBlocks:
    h3text = found.find_element_by_class_name('tag')
    Comparetext = h3text.text
    if Comparetext == 'Date & Time':
        FoundP=found.find_element_by_tag_name('p')
        clearstring = FoundP.text
        clearstring= clearstring.replace('\n',' ')
        print(clearstring)
    #print(found.text)
#page= BeautifulSoup(driver.page_source,'lxml')
#for links in page.find_all('div',class_="extra-block"):
 #   datetag = links.find('h3',class_="tag")
  #  if datetag.get_text() == "Date & Time":
   #     print("found")




# to be updated with new button
# driver.find_element_by_xpath('//button[@class="submit-button__secondary load-more"]').click()
# looks like second extra-block class starts the information
# there always seems to be a date and time but there isnt always a neighborhood or a contact info
# get list of all spans and look at their h3 tags
# tag 'span' tag  h3 if text is Contact Info
# if :
# tag div class body-style + class hidden-body-style
# if :
# tag span tag h3 if text is Date & Time
# if :
# tag span tag h3 If text "Neighborhood: "
# if :
# else if there isn't a h3 tag then the text will be the address
