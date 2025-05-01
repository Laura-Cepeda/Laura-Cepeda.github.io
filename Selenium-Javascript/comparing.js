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
