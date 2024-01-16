from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context(storage_state = ".auth/storage_state.json")
    page = context.new_page()
    page.goto("https://gmail.com")