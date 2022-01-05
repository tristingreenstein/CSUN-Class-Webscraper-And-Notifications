__author__ = "Tristin Greenstein"
__copyright__ = "Copyright (C) 2020 Tristin Greenstein"
__license__ = "Public Domain"
__version__ = "2.0"


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import warnings
from playsound import playsound

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
warnings.filterwarnings("ignore", category=DeprecationWarning) 
outerloop = 0
innerloop = 0
failed_count = 0

# Using Chrome to access web
###WARNING, MUST HAVE GOOGLE CHROME INSTALLED TO USE THIS SOFTWARE###
s = Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=s,options=op)

# Open the website
driver.get('https://cmsweb.csun.edu/psc/CNRPRD/EMPLOYEE/SA/c/NR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL?PortalActualURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fSA%2fc%2fNR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL&PortalContentURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fSA%2fc%2fNR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL&PortalContentProvider=SA&PortalCRefLabel=Class%20Search&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fmynorthridge.csun.edu%2fpsp%2fPANRPRD%2f&PortalURI=https%3a%2f%2fmynorthridge.csun.edu%2fpsc%2fPANRPRD%2f&PortalHostNode=EMPL&NoCrumbs=yes&PortalKeyStruct=yes')

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
time.sleep(0)
def start_program():
    USER_INP = simpledialog.askstring(title="CLASS SELECTION",prompt="INPUT CLASS SELECTION:") # TESTING TO ADD DYNAMIC CLASS SELECTION
    print(USER_INP)
    while outerloop < 1:   
        print("Outerloop Reached:")
        innerloop = 0
        no_crash = 1 # Number of Loops Without Crashing
        while innerloop < 1: ###Main Menu Search Screen###
            if(failed_count > 2):
                restart_browser()
            id_box = driver.find_element_by_id("NR_SSS_SOC_NWRK_SUBJECT")
            id_box.click()
         
            id_box.send_keys('comp') # Selects Comp Sci Major
            id_box.send_keys(Keys.ENTER)
            time.sleep(3)
          
            driver.find_element_by_id("NR_SSS_SOC_NWRK_BASIC_SEARCH_PB").click()
            time.sleep(3)

            ###Loaded All COMP Classes Screen###
            spot_newSection()# Search If New Section Opens
            spot_existingClass()# Search If Spot Opens in Existing Class

            driver.refresh()
            print(no_crash)
            time.sleep(10)
            no_crash+=1
    return

def alarm():
    print("Alarm Triggered: ")
    playsound('audio.mp3')
    outerloop = 2 # Stops while loop.
    innerloop = 2 # Stops while loop.
def spot_newSection():
    try: # Search If New Section Opens
            if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$20").text:
               alarm()
               print(current_time)
            elif '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$20").text:
                print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$20").text + " NO CHANGES")


            if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$21").text:
               alarm()
               print(current_time)
            elif '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$21").text:
                print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$21").text + " NO CHANGES")
    except:
        print("failed " + current_time)
        failed_count +=1
        driver.refresh()
        time.sleep(60)
        innerloop = 2
def spot_existingClass():
    try: # Search If Spot Opens in Existing Class
             driver.find_element_by_id("SOC_DETAIL$21").click()
             time.sleep(1)
             if not '0' in driver.find_element_by_xpath('//*[@id="NR_SSS_SOC_NWRK_AVAILABLE_SEATS$0"]').text:
                alarm()
                print(current_time)
    except:
        print("failed " + current_time)
        failed_count +=1
        driver.refresh()
        time.sleep(10)
        i = 2
def restart_browser():
    failed_count = 0
    driver.close()
    driver.get('https://cmsweb.csun.edu/psc/CNRPRD/EMPLOYEE/SA/c/NR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL?PortalActualURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fSA%2fc%2fNR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL&PortalContentURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fSA%2fc%2fNR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL&PortalContentProvider=SA&PortalCRefLabel=Class%20Search&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fmynorthridge.csun.edu%2fpsp%2fPANRPRD%2f&PortalURI=https%3a%2f%2fmynorthridge.csun.edu%2fpsc%2fPANRPRD%2f&PortalHostNode=EMPL&NoCrumbs=yes&PortalKeyStruct=yes')
def main():
    print("Begin Program: ")
    start_program()
    print("End Program Reached")
if __name__ == "__main__":
    main()