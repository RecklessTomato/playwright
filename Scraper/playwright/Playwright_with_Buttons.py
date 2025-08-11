import random
import time
from playwright.sync_api import sync_playwright, TimeoutError


def scrape_exhibitors(url: str, more_btn: str, card_selector: str, name_selector: str):
    all_exhibitors = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=90000)
        time.sleep(5)

        btn = page.locator(more_btn)
        max_attempts = 3
        while True:

            if btn.count() == 0:
                print("no load-more-button detected")
                break

            clicked = False

            for attempt in range(max_attempts):
                try:
                    print(f"Attempt {attempt + 1}: clicking on button")
                    btn.first.scroll_into_view_if_needed()
                    time.sleep(1.5)
                    btn.first.click(timeout=5000, force=True)
                    clicked = True
                    break
                except TimeoutError:
                    print("timeout on clicking, retry")
                except Exception as e:
                    print(f"clicking failed on attempt {attempt + 1} of {max_attempts}: {e}")
                time.sleep(2)

            if not clicked:
                print("clicking failed after several retires")
                break

            time.sleep(random.uniform(3.5, 5.0))

            cards = page.query_selector_all(card_selector)
            print(f"{len(cards)} detected")
            for card in cards:
                exhibitor = card.query_selector(name_selector)
                if exhibitor:
                    name = exhibitor.inner_text().strip()
                    if name:
                        all_exhibitors.add(name)
    return all_exhibitors
