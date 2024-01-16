from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# service_obj = Service()
ie_options = webdriver.IeOptions()
ie_options.attach_to_edge_chrome = True
ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

driver = webdriver.Ie(options=ie_options)


driver.get('https://bing.com')

time.sleep(2)

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()

