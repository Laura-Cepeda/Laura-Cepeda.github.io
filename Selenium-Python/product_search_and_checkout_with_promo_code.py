"""
-----------------------------------------------------------------------------
QA AUTOMATION SCRIPT REPORT
-----------------------------------------------------------------------------

Test Objective:
  - Validate the end-to-end shopping flow:
    • Search for products with the keyword "ber"
    • Add all visible items to cart
    • Proceed to checkout
    • Apply a valid promo code
    • Confirm promo message is displayed correctly

Test Type:
  - Functional UI Test
  - End-to-End Flow (E2E)
  - Wait Strategy Validation (Implicit + Explicit)

Steps Performed:
  1. Launch Chrome browser and maximize the window.
  2. Apply implicit wait for dynamic content loading.
  3. Navigate to https://rahulshettyacademy.com/seleniumPractise/
  4. Search for products containing the substring "ber".
  5. Wait 3 seconds for results to filter visually (UI update).
  6. Validate the product count and click "Add to Cart" on each result.
  7. Click the cart icon to open the cart.
  8. Click "Proceed to Checkout".
  9. Enter a valid promo code ("rahulshettyacademy") and click "Apply".
 10. Use explicit wait to detect promo confirmation message.
 11. Print the promo response text to the console.
 12. Wait for user input before closing the browser for manual verification.
 13. Quit the browser to clean up the session.

Expected Result:
  - At least one product containing "ber" should be listed.
  - All matching products should be added to the cart.
  - Promo code should apply successfully, showing a confirmation message.
  - No unexpected exceptions or assertion failures should occur.

Notes:
  - Script combines `implicitly_wait` and `WebDriverWait` to handle dynamic loading.
  - `time.sleep(3)` is used to allow UI to update before collecting filtered products.
  - Includes `input()` pause for manual inspection before browser closes.
  - Ensure internet connectivity, as product search is done live.

-----------------------------------------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. Set up Chrome browser using webdriver-manager (automatically downloads latest driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Maximize the browser window before interacting with elements
driver.maximize_window()

# 3. Apply implicit wait globally – Selenium will wait up to 5 seconds for elements to appear
driver.implicitly_wait(5)

# 4. Navigate to the Selenium practice site
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
print(driver.title)  # Print the page title for logging/debugging

# 5. Search for all products containing the keyword "ber"
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# 6. Wait for 3 seconds to allow frontend filtering of product list to complete
time.sleep(3)

# 7. Collect all visible product elements under the results section
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)  # Log number of matching products (3)

# 8. Ensure that there are products found before proceeding
assert count > 0

# 9. Click the "Add to Cart" button for each visible product
for result in results:
    result.find_element(By.XPATH, ".//button").click()

# 10. Click the cart icon to open the mini-cart
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

# 11. Click the "PROCEED TO CHECKOUT" button
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# 12. Enter a valid promo code into the promo field
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# 13. Click the "Apply" promo button
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# 14. Use explicit wait to wait until promo message is visible (up to 15 seconds)
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

# 15. Get and print the confirmation message after promo code is applied
promo_message = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promo_message)

# 16. Optional: pause script for manual verification before closing browser
input("Press Enter to close the browser...")

# 17. Close all browser windows and end session
driver.quit()
