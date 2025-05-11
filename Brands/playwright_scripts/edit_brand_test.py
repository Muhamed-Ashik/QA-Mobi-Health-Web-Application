from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://127.0.0.1:8000/login")
    page.fill('input[name="email"]', "tester@gmail.com")
    page.fill('input[name="password"]', "1234")
    page.click('button:text("Login")')

    page.goto("http://127.0.0.1:8000/admin/brands")
    page.click('a:text("Edit")')
    page.fill('input[name="brand"]', "GooglePixel")
    page.check('input[type="checkbox"]')
    page.click('button:text("Update")')

    page.wait_for_url("http://127.0.0.1:8000/admin/brands")
    print("Brand Updated Successfully")    

    page.close()
