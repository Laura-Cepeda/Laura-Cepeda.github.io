#chrome driver

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager  # Automatically finds and downloads the right ChromeDriver version
# import time  # Used to pause the script so we can see what happens

# Set up ChromeDriver using WebDriver Manager (no need to download manually)
# service_obj = Service(ChromeDriverManager().install())
# # Create a Chrome browser instance using the service
# driver = webdriver.Chrome(service=service_obj)


#Firefox drive
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager  # Auto-manages Firefox driver
# import time
#
# # Set up Firefox driver automatically
# service_obj = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service_obj)



# Microsoft Edge driver using webdriver-manager
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# Use the full path to your manually downloaded msedgedriver.exe
service_obj = Service(r"C:\Users\Stella cepeda\Documents\msedgedriver.exe")

# Create the Edge driver service with that path
driver = webdriver.Edge(service=service_obj)


driver.maximize_window()  # Maximize before loading any page

# Open the first website
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
time.sleep(5)

print(driver.current_url)

# Navigate to another page
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(5)

# Go back to previous page
driver.back()
print(driver.current_url)
time.sleep(5)

driver.quit()  # Close browser and end session cleanly

