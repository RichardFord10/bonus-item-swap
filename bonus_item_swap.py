from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from getpass import getpass
import pandas as pd
import sys
import csv
import os
import re

# configure webdriver & headless chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options = chrome_options, executable_path=r'C:/Users/rford/Desktop/chromedriver/chromedriver.exe')

# current day format
currentDate = datetime.today().strftime('%Y-%m-%d')

#login function
def login(user, pword = str):
    driver.get("https://######.com/manager")
    Username = driver.find_element_by_id("bvuser")
    Password = driver.find_element_by_id("bvpass")
    Login = driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/input')
    Username.send_keys(user)
    Password.send_keys(pword)
    Login.click()
    print("Logging In...")
 
   
#item ids
sale_ids = [
'70280',
'70281',
'72551',
'72552',
'74968',
'74969',
'75729',
'70271',
'70274',
'70273',
]

old_bonus_item = ['238438']
new_bonus_item = ['238605']

#Result Lists
item_results = []

#start function
def switch_bonus_item():
    print('Gathering Information...')
    for sale_id in sale_ids:
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException)
            driver.get("https://www.#######.com/manager/bonus-item-swap.php?sale_id={}&item_id=238438".format(sale_id))
            WebDriverWait(driver, 10)  
            #Navigate to item    
            search_text_id = "search_text"
            WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, search_text_id)))
            driver.find_element_by_xpath('//*[@id="search_text"]').send_keys('item to search for')
            action = ActionChains(driver)
            action.double_click(driver.find_element_by_xpath('/html/body/div[2]/div/select/option[2392]')).perform()
            new_qty_id = "new_qty"
            WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, new_qty_id)))
            driver.find_element_by_xpath('//*[@id="new_qty"]').send_keys('1')
            WebDriverWait(driver, 10)
            driver.find_element_by_xpath('//*[@id="submit-new-bonus"]').click()
            print("Sale {} with bonus item {} has been swapped with bonus item {}".format(sale_id, old_bonus_item, new_bonus_item))
    print('All Sale Bonus Items Switched')


#Run
login(input("Enter Username: "), getpass("Enter Password: "))
switch_bonus_item()
 