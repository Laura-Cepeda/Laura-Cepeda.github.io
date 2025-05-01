// Import the necessary classes from selenium-webdriver
const { Builder, By } = require('selenium-webdriver');

// Function to open Google in Chrome
async function openGoogleInChrome() {
    // Create a new Chrome browser instance
    let driver = await new Builder().forBrowser('chrome').build();
    
    // Navigate to Google's homepage
    await driver.get('https://www.google.com');

    // Maximize the browser window
    await driver.manage().window().maximize();

    // Wait for 3 seconds
    await driver.sleep(3000);

   
    /*Find and click the "Stay signed out" button using the CSS selector .niO4u.VDgVie.SlP8xc
    try {
        const staySignedOutButton = await driver.findElement(By.css('.niO4u.VDgVie.SlP8xc'));
        await staySignedOutButton.click();
    } catch (error) {
        console.error('Could not find or click the "Stay signed out" button using XPath button[aria-label="Stay signed out"]:', error);
    }*/

    //Find and click the "Stay signed out" button using the Xpath selector /html/body/div[1]/div[1]/a[1]
    try {
        const staySignedOutButton = await driver.findElement(By.xpath('/html/body/div[1]/div[1]/a[1]'));
        await staySignedOutButton.click();
    } catch (error) {
        console.error('Could not find or click the "Stay signed out" button using the provided XPath:', error);
    }

     // Wait for a short time after clicking to allow any page changes
     await driver.sleep(1000);
    

    // Close the driver
   // await driver.quit();
}

// Call the function to open Google in Chrome
openGoogleInChrome();

