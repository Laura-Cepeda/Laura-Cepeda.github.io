"""
-----------------------------------------------------------------------------
QA AUTOMATION SCRIPT REPORT
-----------------------------------------------------------------------------

Test Objective:
  - Validate multiple UI interactions on the "Automation Practice" page:
    • Checkbox selection
    • Radio button selection
    • Element visibility toggle
    • JavaScript alert content and behavior

Test Type:
  - Functional UI Test
  - Element State Validation (Checkbox, Radio Button, Input Visibility)
  - JavaScript Alert Handling

Steps Performed:
  1. Launch Chrome browser using webdriver-manager and maximize the window.
  2. Navigate to https://rahulshettyacademy.com/AutomationPractice/.
  3. Locate all checkboxes using CSS selector and select "Option2".
  4. Assert that "Option2" checkbox is selected.
  5. Locate all radio buttons and click on the third option (Radio3).
  6. Assert that Radio3 is selected.
  7. Confirm the visibility of the input field with ID "displayed-text".
  8. Click on the "Hide" button and assert that the field is hidden.
  9. Enter a name into the input box and click the "Alert" button.
 10. Switch to the JavaScript alert, capture and print the message.
 11. Assert that the alert message contains the entered name.
 12. Accept the alert to close it.
 13. Wait for manual inspection before closing the browser.
 14. Close the browser.

Expected Result:
  - Checkbox "Option2" should be selected successfully.
  - Radio button 3 should be selected.
  - Text input should toggle visibility correctly.
  - Alert should display the correct message and accept properly.
  - No errors or failed assertions should occur during test execution.

Notes:
  - Uses `input()` for manual inspection before exit.
  - Uses `assert` statements for test validation.
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
driver.maximize_window()

# 4. Navigate to the Automation Practice page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
time.sleep(5)  # Wait for page to fully load

# 5. Locate all checkboxes and click on the one with value "option2"
checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# 6. Locate all radio buttons and select the third one (Radio3)
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# 7. Validate visibility of the input field before clicking "Hide"
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# 8. Click the "Hide" button and confirm the input field is hidden
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# 9. Enter a name into the input field
name = "laura"
driver.find_element(By.ID, "name").send_keys(name)

# 10. Click the alert button to trigger the JS alert
driver.find_element(By.ID, "alertbtn").click()

# 11. Switch to the alert and capture the alert text
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

# 12. Validate that the alert contains the entered name
assert name in alertText
alert.accept()  # Close the alert

# 13. Wait for manual inspection before closing the browser
input("Press Enter to close the browser...")

# 14. Close the browser
driver.quit()
