"""
-----------------------------------------------------------------------------
Lesson: Handling Multiple Browser Windows with Selenium (Firefox)
-----------------------------------------------------------------------------

Objective:
  - Demonstrate how to:
    • Open a new browser window by clicking a link
    • Switch control between multiple windows
    • Capture and validate text from both the original and new window

Test Type:
  - Functional UI Test
  - Window Handling / Navigation

Steps Performed:
  1. Launch Firefox browser using webdriver-manager and maximize the window.
  2. Apply implicit wait for consistent element loading.
  3. Navigate to https://the-internet.herokuapp.com/windows.
  4. Click the "Click Here" link to open a new window.
  5. Capture all open window handles.
  6. Switch to the newly opened window and extract header text.
  7. Switch back to the original window and extract header text.
  8. Assert that the main window displays the correct title.
  9. Wait for user input before closing the browser.
 10. Close all open windows and end the session.

-----------------------------------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

# 1. Set up Firefox browser using webdriver-manager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# 2. Maximize the browser window before interacting with elements
driver.maximize_window()

# 3. Apply implicit wait globally – Selenium will wait up to 5 seconds for elements to appear
driver.implicitly_wait(5)

# 4. Navigate to the Selenium practice site for window handling
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)  # Print the title of the main window for logging

# 5. Click the "Click Here" link to open a new window
driver.find_element(By.LINK_TEXT, "Click Here").click()

# 6. Capture the window handles (unique IDs for all open browser windows/tabs)
#driver.window_handles is a list of all the window handles (IDs) for every open browser window or tab controlled by Selenium.

windowsOpened = driver.window_handles

# 7. Switch to the new window and print the header text
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

# 8. Switch back to the original window and print the header text
driver.switch_to.window(windowsOpened[0])
main_header = driver.find_element(By.TAG_NAME, "h3").text
print(main_header)

# 9. Validate that the main window displays the expected header
assert main_header == "Opening a new window"

# 10. Pause for manual inspection before closing the browser
input("Press Enter to close the browser...")

# 11. Close all browser windows and end the session
driver.quit()


