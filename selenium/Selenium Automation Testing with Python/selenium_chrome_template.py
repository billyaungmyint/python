from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # to get the browser object
from selenium.webdriver.common.by import By
# if you see select tag , go with Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  # for explicit waits
from selenium.webdriver.support import expected_conditions  # for explicit waits
import time  # for time.sleep

# https://stackoverflow.com/questions/65755603/selenium-ssl-client-socket-impl-cc-handshake-failed
options = webdriver.ChromeOptions()
# to supress all kind of infos, warnings, errors or fatal messages (might suggest using only level 2 for errors)
options.add_argument('log-level=3')
# https://stackoverflow.com/questions/46423361/chrome-devmode-suddenly-turning-on-in-selenium
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # to disable devmode logging
# options.add_argument("--start-maximized")
# options.add_argument("headless")
# options.add_argument("--ignore-cretificate-errors")

# this will take care of the browser exe , if want to be faster, place the path here
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
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
URL = "https://the-internet.herokuapp.com/windows"
driver.get(URL)

# code here


# wait for 2 seconds before closing thee browser
time.sleep(2)
driver.close()  # or use driver.quit()
