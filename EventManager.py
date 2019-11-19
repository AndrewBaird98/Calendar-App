from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os,sys,inspect
import time
from Event import Event
from selenium.common.exceptions import NoSuchElementException


#Event Manager lists
FullEventList = []
SortedEventList = []
CategoriesList = []

def FindEvents():
    if len(FullEventList) == 0:
        current_folder= os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
        chromedriver = os.path.join(current_folder,"chromedriver")

        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        driver.get("https://www.sandiego.org/explore/events.aspx")
        driver.find_element_by_xpath('//button[@class="submit-button__secondary load-more"]').click()
        time.sleep(0.5)
        soup = BeautifulSoup(driver.page_source,'lxml')
        #print(soup)
        eventlist = []
        for links in soup.find_all('section',class_="result"):
            #print(links.find('div', class_="result__tag").get_text())
            E = Event(links.find('a',class_="result__title-link").get_text(),links.find('div',class_="result__dates").get_text(),
                  "Not Know","Not Known","Not Known","Not Known","Not Known", links.find('div',class_="result__tag").get_text(),
                  "Not Know",links.find('a',class_="result__cta-link").get('href'),"Not Known", "Not Known", "Not Known", "Not Known")
            FullEventList.append(E)

        driver.close()
def EventInfoDisplay(EInfo,OutPutBox):
    current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
    chromedriver = os.path.join(current_folder, "chromedriver")
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get(EInfo.link)
    try:
        EventDescription = driver.find_element_by_class_name('header-component__content')
       # print(EventDescription.text)
        OutPutBox.append(EventDescription.text)
    except NoSuchElementException:
        #print("No Other Description found")
        OutPutBox.append("No description found")
    try:
        extraBlocks = driver.find_elements_by_class_name('extra-block')
        extraBlocks.pop(0)
        for found in extraBlocks:
            OutPutBox.append(found.text)
    except NoSuchElementException:
        print("No extra information found")
        pass
    driver.close()
# to be displayed in the UI That way we have one main display
# maybe becomes part of the UI class instead of the event manger class?
def DisplayTheList(List):
    for e in List:
        #To pe printed on to the UI
        e.displayExample()
def SortTheList(Sortby):
    print("hello")
def CollectCategories():
    for e in FullEventList:
        if e.category not in CategoriesList:
            CategoriesList.append(e.category)

if __name__ == '__main__':
    # so it does not run at import and wait to use the functions
    print('should not run')
