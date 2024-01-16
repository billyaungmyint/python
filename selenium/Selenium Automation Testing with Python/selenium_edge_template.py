from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# import time

options = webdriver.EdgeOptions()
options.add_argument('log-level=3') # to supress all kind of infos, warnings, errors or fatal messages (might suggest using only level 2 for errors)
# https://stackoverflow.com/questions/46423361/chrome-devmode-suddenly-turning-on-in-selenium
options.add_experimental_option('excludeSwitches', ['enable-logging']) # to disable devmode logging
# driver = webdriver.Edge(options=options)

service_obj = Service() # this will take care of the browser exe , if want to be faster, place the path here
driver = webdriver.Edge(service=service_obj,options=options)


driver.get("https://rahulshettyacademy.com/") # open the browser

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.close() # close the browser