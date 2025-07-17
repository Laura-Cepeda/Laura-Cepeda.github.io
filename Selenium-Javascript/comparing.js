/**
 * -----------------------------------------------------------------------------
 * QA AUTOMATION SCRIPT REPORT
 * -----------------------------------------------------------------------------
 * Test Objective:
 *   - Validate that the book prices displayed on https://books.toscrape.com/
 *     match the prices stored in a local CSV file (books.csv)
 *   - Identify and log any discrepancies between saved data and current data
 * 
 * Test Type:
 *   - Data-Driven Test
 *   - UI Automation using Selenium WebDriver (Chrome)
 *   - Regression/Validation Check
 * 
 * Steps Performed:
 *   1. Launch Chrome browser
 *   2. Navigate to https://books.toscrape.com/
 *   3. Read book data (Title, Price) from local CSV file (books.csv)
 *   4. Extract current book data from the first 2 pages of the site
 *   5. Compare prices for books found in both the saved CSV and current site
 *   6. Log matched prices and price mismatches
 *   7. Save any discrepancies to a new file (price_discrepancies.csv)
 *   8. Close the browser
 * 
 * Expected Result:
 *   - Each book in the CSV should match the current price shown on the website
 *   - If a mismatch is found, it should be logged and written to price_discrepancies.csv
 *   - Books not found on the website are logged as missing
 * 
 * Notes:
 *   - This script currently supports only Chrome browser
 *   - CSV file must be named "books.csv" and located in the project root
 *   - Prices should be formatted consistently in both the site and CSV
 * -----------------------------------------------------------------------------
 */



// Import the necessary classes from selenium-webdriver
const { Builder, By } = require('selenium-webdriver');
const fs = require('fs');
const csv = require('csv-parser'); // typo fixed: was 'cvs-parser', should be 'csv-parser'

let savedData = [];

// Function to open Google in Chrome
async function openGoogleInChrome() {
    let driver = await new Builder().forBrowser('chrome').build();

    await driver.get('https://books.toscrape.com');
    await driver.manage().window().maximize();
    await driver.sleep(3000);

    // Read data from CSV file
    fs.createReadStream('books.csv') // typo fixed: was 'books.cvs'
        .pipe(csv())
        .on('data', (row) => {
            savedData.push(row);
        })
        .on('end', async () => {
            console.log('CSV file successfully processed.');
            // Proceed after CSV is loaded
            await runPriceVerificationTest(driver);
        });
}

async function runPriceVerificationTest(driver) {
    try {
        let currentData = [];

        // Loop through first two pages
        for (let page = 1; page <= 2; page++) {
            if (page === 1) {
                await driver.get('https://books.toscrape.com/');
            } else {
                await driver.get(`http://books.toscrape.com/catalogue/page-${page}.html`);
                // fixed URL: used template string (backticks) and fixed '.html'
            }

            await driver.sleep(2000);

            let books = await driver.findElements(By.css('article.product_pod'));

            for (let book of books) {
                let titleElement = await book.findElement(By.css('h3 > a'));
                let title = await titleElement.getAttribute('title');

                let priceElement = await book.findElement(By.css('p.price_color'));
                let price = await priceElement.getText();

                currentData.push({ Title: title, Price: price });
            }
        }

        // Compare current data with saved data
        let discrepancies = [];

        for (let i = 0; i < savedData.length; i++) { // typo fixed: 'let i = 0;' was incomplete
            let savedBook = savedData[i];
            let currentBook = currentData.find((book) => book.Title === savedBook.Title);

            if (currentBook) {
                if (currentBook.Price !== savedBook.Price) {
                    discrepancies.push({
                        Title: savedBook.Title,
                        SavedPrice: savedBook.Price,
                        CurrentPrice: currentBook.Price,
                    });
                    console.log(`Price discrepancy found for "${savedBook.Title}": Saved Price = ${savedBook.Price}, Current Price = ${currentBook.Price}`);
                } else {
                    console.log(`Price verified for "${savedBook.Title}": ${savedBook.Price}`);
                }
            } else {
                console.log(`Book not found on the website: ${savedBook.Title}`);
            }
        }

        // Optionally, write discrepancies to a file
        if (discrepancies.length > 0) { // typo fixed: 'legth' -> 'length'
            let discrepancyContent = 'Title,SavedPrice,CurrentPrice\n';
            for (let item of discrepancies) {
                discrepancyContent += `"${item.Title}","${item.SavedPrice}","${item.CurrentPrice}"\n`;
            }
            fs.writeFileSync('price_discrepancies.csv', discrepancyContent);
            console.log('Discrepancies saved to price_discrepancies.csv');
        } else {
            console.log('No price discrepancies found.');
        }
    } catch (error) {
        console.error(error); // typo fixed: 'erroe'
    } finally {
        // Always quit driver
        await driver.quit();
    }
}

// Call the main function
openGoogleInChrome();
