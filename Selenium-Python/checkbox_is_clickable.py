"""
-----------------------------------------------------------------------------
QA AUTOMATION SCRIPT REPORT
-----------------------------------------------------------------------------

Test Objective:
  - Validate that checkboxes on the "Automation Practice" page can be selected.
  - Specifically test selecting "Option2" from the list of checkboxes and ensure
    that it is marked as selected after the click action.

Test Type:
  - Functional UI Test
  - Element Selection Validation (Checkbox)

Steps Performed:
  1. Launch Chrome browser using webdriver-manager and maximize the window.
  2. Navigate to https://rahulshettyacademy.com/AutomationPractice/.
  3. Locate all checkboxes using their common CSS selector.
  4. Iterate through the checkboxes to find one with the value "option2".
  5. Click the checkbox to select it.
  6. Assert that "Option2" is selected after interaction.
  7. Pause the test execution to allow manual browser inspection.
  8. Close the browser.

Expected Result:
  - "Option2" checkbox should be successfully located and clicked.
  - After clicking, the checkbox should remain selected.
  - Script should run without exceptions or failed assertions.

Notes:
  - Script uses `time.sleep()` and `input()` for simplicity and visual inspection.
-----------------------------------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. Setup Chrome WebDriver using webdriver-manager
service_obj = Service(ChromeDriverManager().install())

# 2. Create a Chrome browser instance using the service object
driver = webdriver.Chrome(service=service_obj)

# 3. Maximize the browser window
driver.maximize_window()  # Recommended before interacting with elements

# 4. Navigate to the checkbox practice form
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)  # Print page title to confirm navigation
time.sleep(5)  # Give the page time to load

# 5. Locate all checkboxes on the page using their common CSS selector
checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
print(len(checkboxes))  # Print how many checkboxes were found

# 6. Loop through the checkboxes to find the one with value "option2"
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()  # Select the checkbox
        assert checkbox.is_selected()  # Verify it is now selected
        break  # Exit loop after finding and clicking the correct checkbox

# 7. Wait for manual confirmation before closing the browser
input("Press Enter to close the browser...")

# 8. Close the browser
driver.quit()