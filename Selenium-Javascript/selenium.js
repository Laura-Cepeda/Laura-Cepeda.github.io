/**
 * -----------------------------------------------------------------------------
 * QA AUTOMATION SCRIPT REPORT
 * -----------------------------------------------------------------------------
 * Test Objective:
 *   - Validate that Google's homepage loads correctly in Chrome
 *   - Attempt to locate and click the "Stay signed out" button, if present
 *   - Confirm that the button can be accessed via XPath (as CSS selector may vary)
 * 
 * Test Type:
 *   - Smoke Test / UI Automation
 *   - Environment Validation
 *   - Element Interaction using XPath
 * 
 * Steps Performed:
 *   1. Launch Chrome browser
 *   2. Navigate to https://www.google.com/
 *   3. Maximize the browser window
 *   4. Wait for 3 seconds to ensure the page loads fully
 *   5. Attempt to locate and click the "Stay signed out" button using XPath:
 *      /html/body/div[1]/div[1]/a[1]
 *   6. Log the result (success or error if not found)
 *   7. Wait briefly to observe any resulting action
 *   8. (Optional) Close the browser driver
 * 
 * Expected Result:
 *   - Google homepage should load successfully
 *   - "Stay signed out" button should be clickable if present
 *   - No unhandled errors during script execution
 * 
 * Notes:
 *   - The button may not always appear depending on cookies, location, or login state
 *   - CSS selector version is commented out and may need updates if the DOM structure changes
 *   - Script currently does NOT quit the browser — useful for debugging (can be enabled)
 * -----------------------------------------------------------------------------
 */

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

