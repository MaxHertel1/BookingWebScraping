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

def mainloop(Config):
    #main
    try:
        browser =  webdriver.Chrome(executable_path='chromedriver')
        browser.get(WebObjects.site['Home'])

        btnAcceptCookies = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,WebObjects.objects['BtnAcceptCookies'])))
        btnAcceptCookies.click()

        FieldSearch = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,WebObjects.objects['FieldSearch'])))
        FieldSearch.send_keys(Config.location)
        FieldSearch.send_keys(Keys.RETURN)
    except Exception as e:
        print(e.args)
        sys.exit(0)

    for i in range(0, Config.amount,1):

        xpath = WebObjects.objects['BtnHotelFromTable'].replace('#',str(i))

        # btnHotelFromTable = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,xpath)))

        try:
            hotelUrl = browser.find_element_by_xpath(xpath).get_attribute('href')
        except Exception as e:
            print(e.args)

        browser.get(hotelUrl)
        sleep(1)
        browser.execute_script("window.history.go(-1)")
        sleep(3)


    # browser.close()

if __name__ == "__main__":
    Config = ArgumentHandler(sys.argv[1:])
    mainloop(Config)
    sys.exit(0)