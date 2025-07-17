"""
-----------------------------------------------------------------------------
QA AUTOMATION SCRIPT REPORT
-----------------------------------------------------------------------------

Test Objective:
  - Validate the "Forgot password" flow on https://rahulshettyacademy.com/client.
  - Ensure that an error message appears when "Password" and "Confirm Password" fields do not match.
  - Confirm successful password reset when both fields match.
  - Verify redirection to the login page after successful password update.

Test Type:
  - Functional Test (Negative and Positive Scenarios)
  - UI Automation using Selenium WebDriver (Python)
  - Form Validation and Navigation

Steps Performed:
  1. Launch Chrome browser and maximize window.
  2. Navigate to https://rahulshettyacademy.com/client.
  3. Click on the "Forgot password?" link.
  4. Fill in email field with "demo@gmail.com".
  5. Fill in "Password" field with "Hello@1234".
  6. Fill in "Confirm Password" field with "demo@gmail.com" (mismatched).
  7. Click the "Save New Password" button.
  8. Verify error message: "Password and Confirm Password must match with each other."
  9. Correct the "Confirm Password" to match "Password".
  10. Click the "Save New Password" button again.
  11. Wait and verify that the URL contains "auth/login" indicating redirection to login page.
  12. Wait for user input before closing browser.

Expected Result:
  - Error message appears when passwords do not match.
  - Password update is successful when passwords match.
  - User is redirected to the login page after successful password reset.
  - No unexpected errors occur during execution.

Notes:
  - Script uses webdriver-manager to automatically manage ChromeDriver.
  - Includes explicit wait using time.sleep for demo purposes; can be improved with WebDriverWait.
  - Browser waits for manual confirmation before closing to allow inspection.
  Laura Cepeda
-----------------------------------------------------------------------------
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # Automatically installs the correct driver
import time

# 1. Setup Chrome WebDriver using webdriver-manager
service_obj = Service(ChromeDriverManager().install())
# Create a Chrome browser instance using the service object
driver = webdriver.Chrome(service=service_obj)

# 2. Maximize the browser window
driver.maximize_window()  # Maximize before loading any page

# 3. Navigate to the form page
driver.get("https://rahulshettyacademy.com/client")
print(driver.title)
time.sleep(5)

# 4. Forgot password
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

# 5. Fill  Email
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("demo@gmail.com")

# 5. Fill  Password
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys("Hello@1234")

# 5. Fill  confirm password
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys("demo@gmail.com")

# 6. Click on Button Save Password
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

# 7. Validate error message
# Validate it matches what you
error_element = driver.find_element(By.XPATH, "//div[text()='Password and Confirm Password must match with each other.']")
assert error_element.text == "Password and Confirm Password must match with each other.", "❌ Error message did not match!"

# 8. Re enter confirm password
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").clear()
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys("Hello@1234")

# 9. Click on Button Save Password
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(5)

# 10. validate you land in the correct Url after updating  the password
print("Current URL:", driver.current_url)
assert "auth/login" in driver.current_url, "❌ You did not land on the expected login page!"

#Preventing the browser from closing automatically
input("Press Enter to close browser...")  # waits for you to press Enter
driver.quit()
