// Import the necessary classes from selenium-webdriver
const { Builder, By } = require('selenium-webdriver');
const fs = require('fs');

// Function to open Google in Chrome
async function openGoogleInChrome() {
    // Create a new Chrome browser instance
    let driver = await new Builder().forBrowser('chrome').build();
    
    // Navigate to Google's homepage
    await driver.get('https://books.toscrape.com');

    // Maximize the browser window
    await driver.manage().window().maximize();

    // Wait for 3 seconds
    await driver.sleep(3000);

    // Arrays to store titles and prices
    let titles = [];
    let prices = [];
    
    // Loop through the first 2 pages
    for (let page = 1; page <= 2; page++) {
        // Find all book elements on the page
        let books = await driver.findElements(By.css('.product_pod'));

        // Extract title and price for each book
        for (let book of books) {
            let title = await book.findElement(By.css('h3 a')).getAttribute('title');
            let price = await book.findElement(By.css('.price_color')).getText();
            titles.push(title);
            prices.push(price);
        }

        // Navigate to the next page if not on the last page
        if (page < 2) {
            let nextButton = await driver.findElement(By.css('.next a'));
            await nextButton.click();
            await driver.sleep(2000); // Wait for the next page to load
        }
    }
    // Save the results in a CSV file
    let csvData = 'Title,Price\n';
    titles.forEach((title, index) => {
        csvData += `"${title.replace(/"/g, '""')}",${prices[index]}\n`;
    });
    fs.writeFileSync('books.csv', csvData, 'utf-8');
    console.log('Titles:', titles);
    console.log('Prices:', prices);

    // Close the driver
    //await driver.quit();
}

// Call the function to open Google in Chrome
openGoogleInChrome();

