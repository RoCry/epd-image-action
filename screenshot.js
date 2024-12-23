const puppeteer = require('puppeteer');

async function takeScreenshot(htmlPath, outputPath, viewport) {
    // Parse viewport dimensions
    const [width, height] = viewport.split('x').map(dim => parseInt(dim));
    
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    try {
        const page = await browser.newPage();
        
        // Set viewport
        await page.setViewport({
            width: width,
            height: height
        });

        // Convert local path to file URL if it's a local file
        const url = htmlPath.startsWith('http') 
            ? htmlPath 
            : `file://${require('path').resolve(htmlPath)}`;

        // Navigate to the page
        await page.goto(url, {
            waitUntil: ['networkidle0', 'domcontentloaded']
        });

        // Wait for fonts to load
        await page.evaluateHandle(() => document.fonts.ready);

        // Additional small delay to ensure everything is rendered
        await new Promise(resolve => setTimeout(resolve, 100));

        // Take screenshot
        await page.screenshot({
            path: outputPath,
            fullPage: false
        });

    } finally {
        await browser.close();
    }
}

// Handle command line arguments
const [,, htmlPath, outputPath, viewport] = process.argv;

if (!htmlPath || !outputPath || !viewport) {
    console.error('Usage: node screenshot.js <htmlPath> <outputPath> <viewport>');
    process.exit(1);
}

takeScreenshot(htmlPath, outputPath, viewport)
    .catch(error => {
        console.error('Screenshot error:', error);
        process.exit(1);
    });
