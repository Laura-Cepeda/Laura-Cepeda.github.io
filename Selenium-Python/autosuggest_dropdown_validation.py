"""
-----------------------------------------------------------------------------
QA AUTOMATION SCRIPT REPORT
-----------------------------------------------------------------------------

Test Objective:
  - Validate the dynamic auto-suggestion dropdown functionality on the
    https://rahulshettyacademy.com/dropdownsPractise/ page.
  - Ensure the user can enter a partial country name and select a valid match
    from the dropdown (e.g., "India").

Test Type:
  - Functional UI Test
  - Auto-suggestion List Validation
  - Positive Path Testing

Steps Performed:
  1. Launch Chrome browser using webdriver-manager and maximize the window.
  2. Navigate to the auto-suggestion form page.
  3. Enter partial country name ("ind") into the auto-suggestion field.
  4. Wait for dropdown suggestions to appear.
  5. Loop through available suggestions and select "India" if found.
  6. Validate that "India" is now the selected value in the input field.
  7. Wait for user input before closing the browser.

Expected Result:
  - The auto-suggest dropdown should populate with matching countries.
  - "India" should be selectable from the list and appear as the final value
    in the text input.
  - Script should pass assertion without error.

Notes:
  - This test only covers one valid selection. Additional scenarios (e.g. invalid input, no match) should be tested separately.
  - Script uses `time.sleep()` for demo purposes; recommend `WebDriverWait` for production tests.
  - Manual browser close is controlled by `input()` for test inspection.

-----------------------------------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# 1. Setup Chrome WebDriver using webdriver-manager
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

# 2. Maximize the browser window
driver.maximize_window()

# 3. Navigate to the form page
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.title)
time.sleep(5)  # Give the page time to load completely

# 4. Start typing partial country name into the auto-suggest input field
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)  # Wait for the suggestions to load

# 5. Capture all country suggestions in the dropdown
countries = driver.find_elements(By.XPATH, '//li[@class="ui-menu-item"]//a')
print(len(countries))  # Print the number of suggestions found

# 6. Loop through the list and click on "India" if it exists
for country in countries:
    if country.text == "India":
        country.click()
        break

# 7. Assert that "India" is now the selected value in the input box
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

# 8. Wait for manual inspection before closing the browser
input("Press Enter to close the browser...")
driver.quit()
