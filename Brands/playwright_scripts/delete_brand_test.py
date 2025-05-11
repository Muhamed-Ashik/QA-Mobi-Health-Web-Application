from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("http://127.0.0.1:8000/login")
    page.fill('input[name="email"]', "tester@gmail.com")
    page.fill('input[name="password"]', '1234')
    page.click('button:text("Login")')

    page.goto("http://127.0.0.1:8000/admin/brands")
    brand_locator = page.locator("tr", has_text="GooglePixel")
    delete_button = brand_locator.locator('form button:has-text("Delete")')
    page.once("dialog", lambda dialog: dialog.accept())
    delete_button.wait_for(state="attached", timeout=5000)
    delete_button.click()

    
    page.wait_for_timeout(2000)
    print("Brand Deleted Successfully")
    page.close()