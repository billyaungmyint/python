from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_argument('log-level=3') # to supress all kind of infos, warnings, errors or fatal messages (might suggest using only level 2 for errors)
# https://stackoverflow.com/questions/46423361/chrome-devmode-suddenly-turning-on-in-selenium
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Edge(options=options)

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()