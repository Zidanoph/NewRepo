

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(service=service)
driver.get("https://portal.miuegypt.edu.eg/Index.html#/")
driver.maximize_window()
time.sleep(10)
assert "Python" in driver.title
driver.implicitly_wait(10) # seconds
MyPageTitle=driver.title
driver.find_element_by_xpath('//*[@id="loginModal"]/div[1]/div/div/div').click() #press on Login Button

LogIn = driver.find_element(by=By.XPATH,'//*[@id="loginModal"]/div[1]/div/div/div').click()

print("Hello This is a test for Jenkines")

# main_window_handle = None
# while not main_window_handle:
#     main_window_handle = driver.current_window_handle
# signin_window_handle = None
# while not signin_window_handle:
#     for handle in driver.window_handles:
#         if handle != main_window_handle:
#             signin_window_handle = handle
# driver.switch_to.window(signin_window_ handle)
# #Login
# txtEmail= driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("abdelrahman.zidan@miuegypt.edu.eg")
# driver.implicitly_wait(15)
# NextButton= driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
# driver.implicitly_wait(15)
# txtPassword = driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input').send_keys("AR@mhladis1")
# driver.implicitly_wait(15)
# #End Login



time.sleep(10)
driver.quit()