from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# https://www.browserstack.com/docs/automate/selenium/accept-insecure-certificates#python
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.accept_insecure_certs = True

# https://stackoverflow.com/questions/65755603/selenium-ssl-client-socket-impl-cc-handshake-failed
options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('--ignore-ssl-errors')
options.add_argument('log-level=3')  # to supress all kind of infos, warnings, errors or fatal messages (might suggest using only level 2 for errors)
# https://stackoverflow.com/questions/46423361/chrome-devmode-suddenly-turning-on-in-selenium
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service_obj = Service()
print("start")
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://www.google.com")
print("end")