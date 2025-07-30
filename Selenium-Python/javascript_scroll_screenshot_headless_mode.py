"""
-----------------------------------------------------------------------------
QA AUTOMATION SCRIPT REPORT
-----------------------------------------------------------------------------

Test Objective:
  - Validate the ability to scroll to the bottom of the page using JavaScript
  - Confirm screenshot capture functionality in headless browser mode
  - Demonstrate use of ChromeOptions for headless execution and certificate error handling

Test Type:
  - Functional UI Test
  - Visual Capture Test (Screenshot)
  - Headless Execution Validation

Steps Performed:
  1. Configure Chrome to run in headless mode and ignore SSL certificate errors.
  2. Launch Chrome browser using webdriver-manager.
  3. Maximize the browser window (even in headless mode for full-page rendering).
  4. Navigate to https://rahulshettyacademy.com/AutomationPractice/.
  5. Scroll to the bottom of the page using JavaScript execution.
  6. Capture and save a screenshot of the full page.
  7. Pause execution for manual review (optional).
  8. Close the browser.

Expected Result:
  - Page should load without displaying certificate errors.
  - JavaScript scrolling should bring the viewport to the bottom of the page.
  - Screenshot should be successfully saved as "screen.png".
  - No visible browser window should appear (headless mode).

-----------------------------------------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. Configure Chrome options for headless mode and ignore certificate errors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")  # Run browser in background (no UI)
chrome_options.add_argument("--ignore-certificate-error")  # Bypass certificate warnings

# 2. Setup Chrome WebDriver using webdriver-manager and apply options
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# 3. Maximize the browser window (useful for capturing full-page screenshots)
driver.maximize_window()

# 4. Navigate to the target page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
time.sleep(5)  # Wait for the page to load

# 5. Scroll to the bottom of the page using JavaScript
# Example: window.scrollBy(0,document.body.scrollHeight) scrolls to the bottom or window.scrollBy(0,300)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# 6. Capture a screenshot and save it as 'screen.png' in the current directory
driver.get_screenshot_as_file("screen.png")

# 7. Optional pause for user verification before closing
input("Press Enter to close the window...")

# 8. Close all browser windows and end session
driver.quit()
