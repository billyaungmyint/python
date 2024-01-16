import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# https://stackoverflow.com/questions/75160044/how-to-resolve-this-error-in-selenium-error-couldnt-read-tbscertificate-as-s
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# then add the options to the Chrome
driver = webdriver.Chrome(options=options)
time.sleep(2)

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# <input type="text" name="username" id="username">
# username_locator = driver.find_element(By.XPATH , "//input[@class='username']").send_keys("student")
username_locator = driver.find_element(By.ID , "username")
username_locator.send_keys("student")
time.sleep(2)

# <input type="password" name="password" id="password">
# username_locator = driver.find_element(By.XPATH , "//input[@name='password']").send_keys("Password123")
password_locator = driver.find_element(By.NAME , "password")
password_locator.send_keys("Password123")
time.sleep(2)

# <button id="submit" class="btn">Submit</button>
# submit_button = driver.find_element(By.ID , "submit").click()
submit_button = driver.find_element(By.XPATH , "//button[@class='btn']")
submit_button.click()
time.sleep(2)