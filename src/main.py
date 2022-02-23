from curses import KEY_BREAK
import sys
from selenium import webdriver
from web import WebObjects
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from sys import exit
from time import sleep
from ArgumenHandler import ArgumentHandler
from util import Utilities as util

def mainloop(config):
    #main
    try:
        browser =  webdriver.Chrome(executable_path='chromedriver')
        browser.get(WebObjects.site['Home'])

        btnAcceptCookies = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,WebObjects.objects['BtnAcceptCookies'])))
        btnAcceptCookies.click()

        FieldSearch = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,WebObjects.objects['FieldSearch'])))
        FieldSearch.send_keys(config.location)
        FieldSearch.send_keys(Keys.RETURN)
    except Exception as e:
        print(e.args)
        sys.exit(0)
    i=0
    j=0
    while i < config.amount:
        xpath = WebObjects.objects['BtnHotelFromTable'].replace('#',str(j))

        try:
            hotelUrl = browser.find_element_by_xpath(xpath).get_attribute('href')
            # print(hotelUrl)
            browser.get(hotelUrl)
            sleep(1)
            
            try:
                lblHotelName = browser.find_element_by_xpath(WebObjects.objects['LblHotelName'])
                print(lblHotelName.text)

                TblFacilities = browser.find_element_by_xpath(WebObjects.objects['TblFacilities'])
                listElements = TblFacilities.find_elements_by_tag_name('li')
                
                facilityList=[]
                k = 0
                for elem in listElements:
                    facilityList.append(str(elem.text).replace('\n',' - '))

                # print(facilityList)

            except Exception as e:
                print(e.args)
                sys.exit(0)

            browser.execute_script('window.history.go(-1)')
            sleep(2)
            i = i + 1
        except Exception as e:
            hotelUrl = ''

        j = j + 1

if __name__ == "__main__":
    config = ArgumentHandler(sys.argv[1:])
    mainloop(config)
    sys.exit(0)