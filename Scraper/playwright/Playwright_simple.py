from playwright.sync_api import sync_playwright, TimeoutError
from playwright_stealth import stealth_sync
import time

all_exhibitors = set()


def scroll_to_bottom(page, pause_time=2.0, max_tries=1000):
    last_height = page.evaluate("() => document.body.scrollHeight")

    for i in range(max_tries):
        page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(pause_time)
        new_height = page.evaluate("() => document.body.scrollHeight")

        if new_height == last_height:
            print("no further scrolling... "
                  "start scraping")
            break
        last_height = new_height
    else:
        print("max tries exhausted - no scrolling possible")


def scrape_exhibitors(url: str, selector: str, cards: str, name: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        stealth_sync(page)
        page.goto(url, timeout=120000, wait_until="domcontentloaded")

        scroll_to_bottom(page)

        try:
            page.wait_for_selector(selector, timeout=60000)
        except TimeoutError:
            print(f"timeout on selector {selector}")
            browser.close()
            return

        cards = page.query_selector_all(cards)
        for card in cards:
            h2 = card.query_selector(name)
            if h2:
                ex = h2.inner_text().strip()
                if ex:
                    all_exhibitors.add(ex)

        browser.close()
    return all_exhibitors
