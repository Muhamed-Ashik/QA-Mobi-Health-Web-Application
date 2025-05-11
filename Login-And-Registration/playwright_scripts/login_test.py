from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://127.0.0.1:8000/login")
    page.fill('input[name="email"]', "admin@gmail.com")
    page.fill('input[name="password"]', "1234")
    page.click('button:text("Login")')

    page.wait_for_url("**/admin/dashboard")
    print("Login Success")

