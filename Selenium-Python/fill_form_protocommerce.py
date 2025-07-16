"""
QA Automation Script: Form Submission Test
------------------------------------------

Test Objective:
Automate the process of filling out the user form located at:
https://rahulshettyacademy.com/angularpractice

Steps Performed:
1. Navigate to the target form page.
2. Fill in all required form fields (name, email, password, gender, date of birth, checkbox).
3. Submit the form.
4. Validate that the success message appears after submission.

Test Type:
- Functional UI Test
- Positive Test Case

Expected Result:
- The form should be submitted successfully.
- A success alert should be displayed containing the message:
  "Success! The Form has been submitted successfully!"

Note:
This test is written by a QA Analyst as part of an initial automation project
to validate basic form behavior and visual feedback after user interaction.
Laura Cepeda
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
driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)  #ProtoCommerce
time.sleep(5)

# 📝 4. Fill out the form fields

# 4.1 Enter the name
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("laura QA Test")
# 4.2 Enter the email
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
# 4.3 Enter the password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
# 4.4 Click the checkbox "Check me out if you Love IceCreams!"
driver.find_element(By.ID, "exampleCheck1").click()
# 4.5 Select gender from the dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# 4.6 click on Student on Employment status
driver.find_element(By.XPATH, "//label[@for='inlineRadio1']").click()
# 4.7 Fill date of birth
driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("05/28/1985")
# 4.8 Select the option "Female" by visible text
dropdown.select_by_visible_text("Female")
time.sleep(5)

#5. Submit the form
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#6. Validate the success message appears after form submission
success_message = driver.find_element(By.CLASS_NAME, "alert-success")
# Assertion to check if the message contains expected text
assert "Success! The Form has been submitted successfully!" in success_message.text

time.sleep(30)  # Keeps browser open for 1 minute

# Close all browser windows and end the session to free up system resources
driver.quit()