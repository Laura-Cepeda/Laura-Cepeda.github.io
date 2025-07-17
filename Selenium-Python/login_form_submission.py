""""
Test Objective:
Automate and validate the login and logout functionality on 'https://the-internet.herokuapp.com/'
to ensure users can successfully authenticate and sign out.

Steps Performed:
1. Launch Firefox browser with custom options to disable pop-ups and notifications.
2. Navigate to the homepage.
3. Click on the 'Form Authentication' link.
4. Enter valid username and password.
5. Click the login button.
6. Verify successful login by checking the success message.
7. Click the logout button.
8. Handle any exceptions and close the browser.

Test Type:
Functional Test - Positive Scenario

Expected Result:
User should be able to log in successfully and see a confirmation message, then log out properly.

Note:
- The script uses explicit sleeps for demonstration; consider using explicit waits for better reliability.
- Exceptions are caught to log errors and ensure browser closure.
Laura Cepeda
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Setup Firefox options
options = Options()
options.set_preference("dom.disable_open_during_load", False)  # Disable popup blocking
options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications

# Create a new Firefox browser instance with options
driver = webdriver.Firefox(options=options)

try:
    # Navigate to The Internet homepage
    driver.get('https://the-internet.herokuapp.com/')

    # Maximize the window
    driver.maximize_window()

    # Click the "Form Authentication" link
    form_auth_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    form_auth_link.click()

    # Wait for a few seconds
    time.sleep(3)

    # Enter username
    username_field = driver.find_element(By.XPATH, '//input[@id="username"]')
    username_field.send_keys('tomsmith')

    # Enter password
    password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_field.send_keys('SuperSecretPassword!')

    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')
    login_button.click()

    # Check if login was successful by verifying the presence of the secure area message
    secure_area_message = driver.find_element(By.CSS_SELECTOR, '#flash')
    message_text = secure_area_message.text

    if 'You logged into a secure area!' in message_text:
        print('Login was successful.')
    else:
        print('Login failed.')

    # Wait for a few seconds
    time.sleep(3)

    # Click the logout button
    logout_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/a')
    logout_button.click()

    # Wait for 2 seconds
    time.sleep(2)

except Exception as e:
    print('Error during the automation:', str(e))

finally:
    # Always close the driver
    driver.quit()
