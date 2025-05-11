from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:8000/login")
driver.maximize_window()

driver.find_element(By.Name, "email").send_keys("admin@gmail.com")
driver.find_element(By.Name, "password").send_keys("1234")
driver.find_element(By.XPATH, '//button[text()="Login"]').click()
time.sleep(2)

driver.get("http://127.0.0.1:8000/admin/brands/add_new")
time.sleep(1)

driver.find_element(By.Name, "brand").send_keys("Apple")
driver.find_element(By.Name, "status").send_keys(1)

#driver.find_element(By.Name, "status").send_keys(0)

driver.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(2)
if "admin/brands" in driver.current_url:
    print("Brand Added Succesfully")
else:
    print("Failed to Add Brand")

driver.quit()
