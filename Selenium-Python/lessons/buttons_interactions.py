"""
-----------------------------------------------------------------------------
Lesson: Selenium ActionChains – Hover, Right-Click, and Move-to-Element
-----------------------------------------------------------------------------

Objective:
  This lesson demonstrates how to use Selenium's ActionChains class to:
  - Hover over a menu item to reveal hidden options
  - Perform a right-click (context click) on a submenu item
  - Move to another option and click it

-----------------------------------------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. Setup Chrome WebDriver using webdriver-manager
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

# 2. Maximize the browser window
driver.maximize_window()

# 3. Navigate to the Automation Practice page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
time.sleep(5)  # Wait for the page to fully load

# 4. Initialize ActionChains for advanced user interactions
action = ActionChains(driver)

# 5. Hover over the "Mouse Hover" menu to reveal hidden options
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# 6. Perform a right-click (context click) on the "Top" option
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

# 7. Move to the "Reload" option and left-click on it
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# 8. Pause for manual verification before closing the browser
input("Press Enter to close the browser...")

# 9. Close the browser and end the session
driver.quit()