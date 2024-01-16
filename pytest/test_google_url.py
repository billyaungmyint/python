import pytest
from selenium import webdriver

# Fixture to set up the browser
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test function to open Google and get the page title
def test_open_google_and_get_title(browser):
    browser.get("https://www.google.com")
    title = browser.title
    print("Page Title:", title)

# You can run this test using pytest
# Just save this code to a .py file and run 'pytest <filename>.py' in your terminal
