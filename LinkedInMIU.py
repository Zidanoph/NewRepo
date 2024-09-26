import time


from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC



# driver=webdriver.Edge()


driver=webdriver.Chrome()


driver.get("https://portal.miuegypt.edu.eg")


driver.maximize_window()
print(driver.title)
print(driver.current_url)
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle
signing_window_handle = None
while not signing_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signing_window_handle = handle
            break  # Exit the loop once the sign-in window is found
driver.switch_to.window(signing_window_handle)

element = driver.find_element(By.XPATH, "//*[@id='loginModal']/div[1]/div[2]/div").click()
 






time.sleep(25) 