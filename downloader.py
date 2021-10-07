import time
import os
from variables import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# Set the default download location on chrome

import chromedriver_autoinstaller

# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path
chromedriver_autoinstaller.install()  

# Initialize the translations directory
dir = os.path.join(path, trans_dir)
if not os.path.exists(dir):
    os.mkdir(dir)

# Set the default path to download the texts in to
# make sure it leads to the same directory as the program
chrome_options = webdriver.ChromeOptions()
preferences = {"download.default_directory": path+trans_dir,
                "directory_upgrade": True,
                "safebrowsing.enabled": True }
chrome_options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=chrome_options)
driver.delete_all_cookies()

# Login to law site
driver.get('http://www.japaneselawtranslation.go.jp/law/?re=2')
# Click on the second menu
search_1 = driver.find_element_by_xpath("//*[contains(text(), '投資')]").click()
time.sleep(1)

# Open the list of downloaded documents as a string\
'''
# Use this if you already have a list_of_documents.txt file

with open('list_of_documents.txt', 'r') as f1:
    docs = []
    for doc in f1.readlines():
        docs.append(doc[:-1])
'''

downloaded = []
# Chooses the first page of results by default.
# The indices for the pages will be [-10 to -3]
#driver.find_elements_by_tag_name("a")[-6].click() # Pick a page among the pages of search results. 
while True:
    # Get the second <ul> element
    document_list = driver.find_elements_by_tag_name('ul')[1]
    # List all the documents in the list
    items = document_list.find_elements_by_tag_name("li")

    # Get the window with the search results as the base window
    base_window = driver.current_window_handle
    for item in items:
        # Check if the document has the default format, skip if it doesn't
        if len(item.find_elements_by_tag_name('img')) > 0:
            continue
        # Check if the document has already been downloaded
        '''
        # Use this if you already have a list_of_documents.txt file
        
        in_list = False
        title = str(item.find_elements_by_tag_name('a')[0].get_attribute('text'))[28:-10]
        for d in docs:
            print(d)
            title = str(item.find_elements_by_tag_name('a')[0].get_attribute('text'))[28:28+len(d)-1]
            print(title)
            if d[:-1] in title:
                in_list = True
                break
        if in_list == True:
            continue
        '''
        # Click on the link associated with the document
        item.find_element_by_tag_name("a").click()
        for w in driver.window_handles:
        #switch focus to child window
            if (w!=base_window):
                driver.switch_to.window(w)

        divs = driver.find_elements_by_tag_name('div')
        # Go to the footer div to access the downloads
        footer = driver.find_elements_by_class_name('footer')[0]
        # Dig deeper until the download button has been reached
        driver.switch_to.frame("footerFrame")
        lf = driver.find_element_by_id('lawsFooter')
        dl = lf.find_element_by_id('dateDl')
        form = dl.find_element_by_name('law_dl')
        # Download the files for the english and japanese translations
        select_object = Select(form.find_element_by_name('ff'))
        select_object.select_by_value('03')
        download_button = driver.find_elements_by_tag_name("input")[1].click()
        # Switch to the alert button that pops up and accept it
        obj = driver.switch_to.alert
        obj.accept()
        time.sleep(1)
        # Do the same for english translations
        select_object.select_by_value('08')
        download_button = driver.find_elements_by_tag_name("input")[1].click()
        obj = driver.switch_to.alert
        obj.accept()
        time.sleep(1)
        driver.close()
        driver.switch_to.window(base_window)
    # Move to the next page of search results
    driver.find_elements_by_tag_name("a")[-2].click()
