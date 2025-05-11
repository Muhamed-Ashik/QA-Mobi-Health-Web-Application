from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()


    page.goto("http://127.0.0.1:8000/register")

    page.fill('input[name="name"]', "Tester")
    page.fill('textarea[name="address"]', "Gampola, Kandy", timeout=5000)

    page.fill('input[name="phone"]', "1234567890")
    page.fill('input[name="email"]', "tester@gmail.com")
    page.fill('input[name="password"]', "1234")
    page.fill('input[name="password_confirmation"]', "1234")
    page.click('button:text("Register")')

    page.wait_for_url("**/")
    print("User Account Registered")

    browser.close()