from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find search box
search = driver.find_element(By.NAME, "q")

# Perform search
search.send_keys("Test Automation")
search.send_keys(Keys.RETURN)

time.sleep(3)

# Validate title contains keyword
assert "Test Automation" in driver.title

print("Test Passed!")

driver.quit()
