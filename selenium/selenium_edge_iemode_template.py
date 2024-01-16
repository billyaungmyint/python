from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # to get the browser object
from selenium.webdriver.common.by import By
# if you see select tag , go with Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  # for explicit waits
from selenium.webdriver.support import expected_conditions  # for explicit waits
import time  # for time.sleep

ie_options = webdriver.IeOptions()
ie_options.attach_to_edge_chrome = True
ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

driver = webdriver.Ie(options=ie_options)

# global timeout - implicit - good to have both explicit and implicit wait ...
driver.implicitly_wait(5)
# only 10 sec for this element
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located(
#     By.CSS_SELECTOR, ".promoInfo"))

# if classname then starts with . , id then starts with #
# driver.find_element(By.CSS_SELECTOR , "#name").send_keys(name)
# driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# if CSS_SELECTOR then space and no // or @ , if XPATH then //[@]/
# driver.find_elements(By.XPATH, "//div[@class='products']/div")
# driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")


# maximise the browser
driver.maximize_window()
# go to the site
URL = "https://www.google.com.sg"
driver.get(URL)

time.sleep(2)
driver.close() # or driver.close() wont work unless the site must be loaded in iemode
