from selenium import webdriver # import web driver
from selenium.webdriver.chrome.service import Service # import service
from selenium.webdriver.common.by import By #import by
import time #import time


service = Service("chromedriver.exe") #chrome driver
driver = webdriver.Chrome(service=service) 


driver.get("http://127.0.0.1:8000/login") #open the login page
driver.maximize_window()


driver.find_element(By.NAME, "email").send_keys("aadmin@gmail.com") # fill the email field sample data
driver.find_element(By.NAME, "password").send_keys("12456") # fill the password field sample data


#driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div[2]/div/div[2]/form/div[3]/button').click()

driver.find_element(By.XPATH, '//*[@type="submit"]').click() # click login where it contains submit


# Wait and check result
time.sleep(5) # hold for 5s
print("Current URL:", driver.current_url) # priting the current url 

if "admin/dashboard" in driver.current_url: # url contains admin/dashboard print follwings
    print("Login Successful!")
else:
    print("Login Failed")

driver.quit() #quit the driver
