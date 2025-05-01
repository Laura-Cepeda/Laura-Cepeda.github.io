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
        await usernameField.sendKeys('tomsmithh'); //incorrect username to test error handling 'tomsmith
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
            // Take a screenshot for successful login
            let screenshot = await driver.takeScreenshot();
            require('fs').writeFileSync('successful_login.png', screenshot, 'base64');
        } else {
            console.log('Login failed.');
            // Take a screenshot for failed login
            let screenshot = await driver.takeScreenshot();
            require('fs').writeFileSync('failed_login.png', screenshot, 'base64');
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
