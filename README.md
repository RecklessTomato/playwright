# 🕷️ Playwright Web Scraper – Scroll & Load More Variants

This project contains two modular web scrapers built with [Microsoft Playwright](https://playwright.dev/python/), designed to extract data from websites that load content either by **scrolling** or via a **"Load More" button**.

It’s ideal for scraping exhibitor directories, product lists, or any dynamically rendered content.

---

## 🚀 Features

- ✅ Handles infinite scrolling pages
- ✅ Supports "Load More" button logic
- ✅ Uses `playwright-stealth` to avoid bot detection
- ✅ Modular and easy to plug into larger scraping pipelines
- ✅ Outputs unique results via a `set` to avoid duplicates

---

## 🧱 Project Structure

```text
Scraper/
└── playwright/
    ├── Playwright_simple.py            # For infinite scroll pages
    ├── Playwright_with_Buttons.py     # For "Load More" button pages
    ├── playwright_scraper.py          # Main runner script
