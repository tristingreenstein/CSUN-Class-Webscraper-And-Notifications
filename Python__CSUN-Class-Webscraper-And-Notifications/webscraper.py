from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from playsound import playsound
x = 0

# Using Chrome to access web
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
# Open the website
driver.get('https://cmsweb.csun.edu/psc/CNRPRD/EMPLOYEE/SA/c/NR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL?PortalActualURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fSA%2fc%2fNR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL&PortalContentURL=https%3a%2f%2fcmsweb.csun.edu%2fpsc%2fCNRPRD%2fEMPLOYEE%2fSA%2fc%2fNR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL&PortalContentProvider=SA&PortalCRefLabel=Class%20Search&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fmynorthridge.csun.edu%2fpsp%2fPANRPRD%2f&PortalURI=https%3a%2f%2fmynorthridge.csun.edu%2fpsc%2fPANRPRD%2f&PortalHostNode=EMPL&NoCrumbs=yes&PortalKeyStruct=yes')
time.sleep(0)

val = input("Enter your value: ")
print(val)
while x < 1:   
   # Select the id box
   i = 0
   j = 1
   while i < 1:
      # Main Menu Search Screen
      t = time.localtime()
      current_time = time.strftime("%H:%M:%S", t)
      id_box = driver.find_element_by_id("NR_SSS_SOC_NWRK_SUBJECT")
      id_box.click()
         
      id_box.send_keys('comp')
      id_box.send_keys(Keys.ENTER)
      time.sleep(3)
      #Loaded All COMP Classes Screen
      driver.find_element_by_id("NR_SSS_SOC_NWRK_BASIC_SEARCH_PB").click()
      time.sleep(3)
      try: #Search If New Section Opens
         if not '( 2 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$20").text:
            playsound('audio.mp3')
            print(current_time)
         if not '( 3 Sections )' in driver.find_element_by_id("NR_SSS_SOC_NWRK_DESCR15$21").text:
            playsound('audio.mp3')
            print(current_time)
      except:
         print("failed " + current_time)
         driver.refresh()
         time.sleep(60)
         break
      try: #Search If Spot Opens in Existing Class
         driver.find_element_by_id("SOC_DETAIL$21").click()
         time.sleep(1)
         if not '0' in driver.find_element_by_xpath('//*[@id="NR_SSS_SOC_NWRK_AVAILABLE_SEATS$0"]').text:
            playsound('audio.mp3')
            print(current_time)
         #if not '0' in
         #driver.find_element_by_id("NR_SSS_SOC_NWRK_AVAILABLE_SEATS$1").text:
         #   playsound('audio.mp3')
         #   print(current_time)
      except:
         print("failed " + current_time)
         driver.refresh()
         time.sleep(60)
         break              
      driver.refresh()
      print(j)
      time.sleep(60)
      j+=1