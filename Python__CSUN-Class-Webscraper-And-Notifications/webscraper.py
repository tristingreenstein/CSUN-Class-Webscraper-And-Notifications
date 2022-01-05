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
LOOP_SPEED = 100 # Speed in Seconds for rechecking class search

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
            time.sleep(2)
          
            driver.find_element_by_id("NR_SSS_SOC_NWRK_BASIC_SEARCH_PB").click()
            time.sleep(3)

            ###Loaded All COMP Classes Screen###
            spot_newSection()# Search If New Section Opens
            driver.refresh()
            time.sleep(3)


            id_box = driver.find_element_by_id("NR_SSS_SOC_NWRK_SUBJECT")
            id_box.click()
            time.sleep(2)
            id_box.send_keys('comp') # Selects Comp Sci Major
            id_box.send_keys(Keys.ENTER)
            time.sleep(2)
            driver.find_element_by_id("NR_SSS_SOC_NWRK_CHECK_BOX").click()
            time.sleep(2)
            driver.find_element_by_id("NR_SSS_SOC_NWRK_BASIC_SEARCH_PB").click()
            time.sleep(2)
            spot_existingClass()# Search If Spot Opens in Existing Class

            driver.refresh()
            print(no_crash)
            time.sleep(LOOP_SPEED)
            no_crash+=1
    return

def alarm():
    print("Alarm Triggered: ")
    playsound('audio.mp3')
    outerloop = 2 # Stops while loop.
    innerloop = 2 # Stops while loop.
def spot_newSection():
    try: # Search If New Section Opens
        all_classes()
    except:
        print("failed " + current_time)
        failed_count +=1
        driver.refresh()
        time.sleep(60)
        innerloop = 2
def all_classes():
    ##110
    if not '( 7 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$2").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$2").text + " NEW SECTION")

    ##122
    if not '( 6 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$6").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$6").text + " NEW SECTION")

    ##182
    if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$8").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$8").text + " NEW SECTION")

    ##222
    if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$10").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$10").text + " NEW SECTION")

    ##256
    if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$11").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$11").text + " NEW SECTION")

    ##282
    if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$13").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$13").text + " NEW SECTION")

    ##310
    if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$15").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$15").text + " NEW SECTION")

    ##322
    if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$16").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$16").text + " NEW SECTION")

    ##333
    if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$18").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$18").text + " NEW SECTION")

    ##380
    if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$19").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$19").text + " NEW SECTION")

    ##424
    if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$21").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$21").text + " NEW SECTION")

    ##429
    if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$22").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$22").text + " NEW SECTION")

    ##430
    if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$23").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$23").text + " NEW SECTION")

    ##440
    if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$24").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$24").text + " NEW SECTION")

    ##469
    if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$25").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$25").text + " NEW SECTION")

    ##482
    if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$26").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$26").text + " NEW SECTION")

    ##484
    if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$27").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$27").text + " NEW SECTION")

    ##485
    if not '( 6 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$29").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$29").text + " NEW SECTION")

    ##522
    if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$31").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$31").text + " NEW SECTION")

    ##541
    if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$32").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$32").text + " NEW SECTION")

    ##542
    if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$33").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$33").text + " NEW SECTION")

    ##560
    if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$34").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$34").text + " NEW SECTION")

    ##565
    if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$35").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$35").text + " NEW SECTION")

    ##583
    if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$36").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$36").text + " NEW SECTION")

    ##584
    if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$37").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$37").text + " NEW SECTION")

    ##587
    if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$38").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$38").text + " NEW SECTION")

    ##589
    if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$39").text:
        print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$39").text + " NEW SECTION")
def specific_class(num:int):
    if(num == 110):
        ##110
        if not '( 7 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$2").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$2").text + " NEW SECTION")
    if(num == 122):
        ##122
        if not '( 6 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$6").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$6").text + " NEW SECTION")
    if(num == 182):
        ##182
        if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$8").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$8").text + " NEW SECTION")
    if(num == 222):
        ##222
        if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$10").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$10").text + " NEW SECTION")
    if(num == 256):
        ##256
        if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$11").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$11").text + " NEW SECTION")
    if(num == 282):
        ##282
        if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$13").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$13").text + " NEW SECTION")
    if(num == 310):
        ##310
        if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$15").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$15").text + " NEW SECTION")
    if(num == 322):
        ##322
        if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$16").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$16").text + " NEW SECTION")
    if(num == 333):
        ##333
        if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$18").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$18").text + " NEW SECTION")
    if(num == 380):
        ##380
        if not '( 5 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$19").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$19").text + " NEW SECTION")
    if(num == 424):
        ##424
        if not '( 4 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$21").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$21").text + " NEW SECTION")
    if(num == 429):
        ##429
        if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$22").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$22").text + " NEW SECTION")
    if(num == 430):
        ##430
        if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$23").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$23").text + " NEW SECTION")
    if(num == 440):
        ##440
        if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$24").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$24").text + " NEW SECTION")
    if(num == 469):
        ##469
        if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$25").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$25").text + " NEW SECTION")
    if(num == 482):
        ##482
        if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$26").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$26").text + " NEW SECTION")
    if(num == 484):
        ##484
        if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$27").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$27").text + " NEW SECTION")
    if(num == 485):
        ##485
        if not '( 6 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$29").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$29").text + " NEW SECTION")
    if(num == 522):
        ##522
        if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$31").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$31").text + " NEW SECTION")
    if(num == 541):
        ##541
        if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$32").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$32").text + " NEW SECTION")
    if(num == 542):
        ##542
        if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$33").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$33").text + " NEW SECTION")
    if(num == 560):
        ##560
        if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$34").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$34").text + " NEW SECTION")
    if(num == 565):
        ##565
        if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$35").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$35").text + " NEW SECTION")
    if(num == 583):
        ##583
        if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$36").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$36").text + " NEW SECTION")
    if(num == 584):
        ##584
        if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$37").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$37").text + " NEW SECTION")
    if(num == 587):
        ##587
        if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$38").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$38").text + " NEW SECTION")
    if(num == 589):
        ##589
        if not '( 1 Section )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$39").text:
            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$39").text + " NEW SECTION")
def spot_existingClass():
    try: # Search If Spot Opens in Existing Class
            #driver.find_element_by_id("SOC_DETAIL$21").click()
            # time.sleep(1)
                    # if not '0' in
                            # driver.find_element_by_xpath('//*[@id="NR_SSS_SOC_NWRK_AVAILABLE_SEATS$0"]').text:
            #     alarm()
                    #     print(current_time)
            # elif '0' in
                    # driver.find_element_by_xpath('//*[@id="NR_SSS_SOC_NWRK_AVAILABLE_SEATS$0"]').text:
            #     print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$21").text
                    #     + " NO CHANGE IN SECTION: " +
                            #     driver.find_element_by_id("NR_SSS_SOC_NSEC_CLASS_SECTION$0").text)
        try:
            if(driver.find_element_by_id("SOC_DETAIL$16")):
                print("NEW SPOT OPEN")
                arr = ['100','108','111B','111BL','122','122L','222','282','300','380L','485','491L','560','565','696C','698C']
                for w in range(len(arr)):
                    timer = 0
                    for className in arr:
                        if className in driver.find_element_by_id(f'NR_SSS_SOC_NWRK_DESCR100_2${w}').text:
                            break
                        if timer == len(arr) - 1:
                            print(driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR100_2$0").text)
                        timer += 1
        except:
            print()
    except:
        print("failed " + current_time)
        failed_count += 1
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