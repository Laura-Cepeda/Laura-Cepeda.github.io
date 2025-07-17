/**
 * -----------------------------------------------------------------------------
 * QA AUTOMATION SCRIPT REPORT
 * -----------------------------------------------------------------------------
 * Test Objective:
 *   - Verify that a user can successfully log in to the secure area of 
 *     "The Internet" web application using valid credentials.
 *   - Confirm that the secure area message appears after successful login.
 * 
 * Test Type:
 *   - Functional Test (Positive Scenario)
 *   - UI Automation using Selenium WebDriver (Chrome)
 * 
 * Steps Performed:
 *   1. Launch Chrome browser with custom options to disable popups and notifications
 *   2. Navigate to https://the-internet.herokuapp.com/
 *   3. Click on the "Form Authentication" link
 *   4. Enter valid username: "tomsmith"
 *   5. Enter valid password: "SuperSecretPassword!"
 *   6. Click the login button
 *   7. Verify that the success message contains: "You logged into a secure area!"
 *   8. If login is successful, log a success message to the console
 *   9. Click the logout button to return to the homepage
 *  10. Close the browser
 * 
 * Expected Result:
 *   - Application should allow login with valid credentials
 *   - A success message should be displayed after login
 *   - The user should be redirected to the secure area
 * 
 * Notes:
 *   - This script is configured to run in Chrome only
 *   - This test focuses only on the *positive* login path
 *   - Credentials used are provided by the practice site
 *     (https://the-internet.herokuapp.com/login)
 * -----------------------------------------------------------------------------
 */

// Import the necessary classes from selenium-webdriver
const { Builder, By } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

// Function to open the secure area
async function openSecureArea() {
    // Setup Chrome options to disable popups
    let options = new chrome.Options();
    options.addArguments('--disable-popup-blocking');
    options.addArguments('--disable-notifications');
    options.addArguments('--disable-password-manager-reauthentication');

    // Create a new Chrome browser instance with options
    let driver = await new Builder()
        .forBrowser('chrome')
        .setChromeOptions(options)
        .build();

    try {
        // Navigate to The Internet homepage
        await driver.get('https://the-internet.herokuapp.com/');

        // Maximize the window
        await driver.manage().window().maximize();

        // Click the "Form Authentication" link
        let formAuthLink = await driver.findElement(By.css('a[href="/login"]'));
        await formAuthLink.click();

        // Wait for a few seconds
        await driver.sleep(3000);

        // Enter username
        let usernameField = await driver.findElement(By.xpath('//input[@id="username"]'));
        await usernameField.sendKeys('tomsmith'); 

        // Enter password
        let passwordField = await driver.findElement(By.xpath('//input[@id="password"]'));
        await passwordField.sendKeys('SuperSecretPassword!');

        // Click the login button
        let loginButton = await driver.findElement(By.css('.fa.fa-2x.fa-sign-in'));
        await loginButton.click();
        // Check if login was successful by verifying the presence of the secure area message
        let secureAreaMessage = await driver.findElement(By.css('#flash'));
        let messageText = await secureAreaMessage.getText();

        if (messageText.includes('You logged into a secure area!')) {
            console.log('Login was successful.');
        } else {
            console.log('Login failed.');
        }

        // Wait for a few seconds
        await driver.sleep(3000);

        // Click the logout button
        let logoutButton = await driver.findElement(By.xpath('//*[@id="content"]/div/a'));
        await logoutButton.click();

        // Wait for 2 seconds
        await driver.sleep(2000);

    } catch (error) {
        console.error('Error during the automation:', error);
    } finally {
        // Always close the driver
        await driver.quit();
    }
}

// Call the function
openSecureArea();
