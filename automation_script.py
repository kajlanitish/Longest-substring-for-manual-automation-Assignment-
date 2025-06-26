from selenium import webdriver
from selenium.webdriver.common.by import By

# Browser Initialization
driver = webdriver.Chrome()
driver.get("https://agrichain.com/qa/input")

# Test Steps
driver.find_element(By.ID, "stringInput").send_keys("abcabcbb")
driver.find_element(By.ID, "submitButton").click()

# Assertion
result = driver.find_element(By.ID, "resultOutput").text
assert result == "3", f"Expected '3' but got {result}"

driver.quit()
