from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os,sys,inspect
import time
from Event import Event
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException


#Event Manager lists
FullEventList = []

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
        LoadMore = driver.find_element_by_xpath('//button[@class="submit-button__secondary load-more"]')
        LoadMore.click()
        time.sleep(0.3)
        LoadMore.click()
        time.sleep(0.3)
        soup = BeautifulSoup(driver.page_source,'lxml')
        #print(soup)
        eventlist = []
        for links in soup.find_all('section',class_="result"):
            #print(links.find('div', class_="result__tag").get_text())
            E = Event(links.find('a',class_="result__title-link").get_text(), links.find('div',class_="result__dates").get_text(),
                  "No Location","Not Know","Not Know", "not Know",links.find('div',class_="result__tag").get_text(),"Not Known",
                   links.find('a',class_="result__cta-link").get('href'),"Not Filled","Not Contact", "No DateTime")
            FullEventList.append(E)

        driver.close()
def EventInfoDisplay(EInfo,popup,PassedList,index):
   if EInfo.Filled == "Not Filled":
        current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
        chromedriver = os.path.join(current_folder, "chromedriver")
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        driver.get(EInfo.link)
        CompletedEvent = EInfo
        try:

            LoadMore = driver.find_element_by_class_name('off').click()
            time.sleep(1)
            EventDescription = driver.find_element_by_class_name('header-component__content opened')
             # print(EventDescription.text)
            CompletedEvent.description = EventDescription.text
            popup.append(EventDescription.text)
        except NoSuchElementException:
             #print("No Other Description found")
            EventDescription = driver.find_element_by_class_name('header-component__content')
            CompletedEvent.description = EventDescription.text
            popup.append(EventDescription.text)
            #popup.append("No description found")
        try:
            extraBlocks = driver.find_elements_by_class_name('extra-block')
            extraBlocks.pop(0)
            Location = extraBlocks[0]
            try:
                h3Check = Location.find_element_by_tag_name('h3')
                compareText = h3Check.text
                #print(compareText)
                if "Neighborhood:" in compareText:
                    CompletedEvent.location = Location.text
                    popup.append(CompletedEvent.location)
                    extraBlocks.pop(0)
                else:
                    popup.append("no location")
            except NoSuchElementException:
                CompletedEvent.location = Location.text
                popup.append(CompletedEvent.location)
                extraBlocks.pop(0)
            for found in extraBlocks:
                hcheck = found.find_element_by_class_name('tag')
                if hcheck.text == "Contact Info":
                    CompletedEvent.Contact = found.text
                    popup.append(CompletedEvent.Contact)
                elif hcheck.text == "Date & Time":
                    CompletedEvent.DateTime = found.text
                    popup.append(CompletedEvent.DateTime)
                elif hcheck.text == "Price":
                    CompletedEvent.price = found.text
                    popup.append(CompletedEvent.price)
        except NoSuchElementException:
            print("No extra information found")
            pass
        CompletedEvent.Filled = "Filled"
        PassedList[index] = CompletedEvent
        driver.close()
   else :
       popup.append(EInfo.description)
       popup.append(EInfo.location)
       popup.append(EInfo.Contact)
       popup.append(EInfo.DateTime)
       popup.append(EInfo.price)



#if __name__ == '__main__':
    # so it does not run at import and wait to use the functions since web scraper takes time
    #print('should not run')
