""""
-----------------------------------------------------------------------------
Lesson: Working with iFrames in Selenium (Firefox)

Objective:
  This lesson demonstrates how to:
  - Navigate into an iframe on a web page
  - Clear and write text inside the iframe
  - Switch back to the main (default) content

Important:
  The TinyMCE editor used in this demo may enter read-only mode if your monthly
  usage limit is reached. If text input does not work, the editor is likely locked.


-----------------------------------------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

# 1. Set up Firefox WebDriver using GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# 2. Maximize the browser window
driver.maximize_window()

# 3. Set an implicit wait (applies globally)
driver.implicitly_wait(2)

# 4. Navigate to the page with the embedded iframe editor
driver.get("https://the-internet.herokuapp.com/iframe")
print(driver.title)  # Print the page title for verification

# 5. Switch Selenium's context to the iframe by its name attribute
driver.switch_to.frame("mce_0_ifr")

# 6. Use explicit wait to ensure the iframe content is fully loaded
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#mce_0_ifr")))

# 7. Clear existing text from the TinyMCE editor
# Note: If the editor is locked (read-only), this step will not work
driver.find_element(By.ID, "tinymce").clear()

# 8. Enter new text into the editor
driver.find_element(By.ID, "tinymce").send_keys("Laura testing iFrame")

# 9. Switch back to the main (default) page content
driver.switch_to.default_content()

# 10. Print the heading text from the main page
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

# 11. Pause for manual inspection before closing the browser
input("Press Enter to close the browser...")

# 12. Close the browser and end the session
driver.quit()
