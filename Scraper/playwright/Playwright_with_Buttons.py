import random
import time
from playwright.sync_api import sync_playwright, TimeoutError


def scrape_exhibitors(url: str, more_btn: str, cards: str, name: str):
    all_exhibitors = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=90000)
        time.sleep(5)

        max_attempts = 3

        while True:

            if more_btn.count() == 0:
                print("no load-more-button detected")
                break

            clicked = False

            for attempt in range(max_attempts):
                try:
                    print(f"Attempt {attempt + 1}: clicking on button")
                    more_btn.first.scroll_into_view_if_needed()
                    time.sleep(1.5)
                    more_btn.first.click(timeout=5000, force=True)
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

            cards = page.query_selector_all(cards)
            print(f"{len(cards)} detected")
            for card in cards:
                h2 = card.query_selector(name)
                if h2:
                    name = h2.inner_text().strip()
                    if name:
                        all_exhibitors.add(name)

        print(f"\n {len(all_exhibitors)} total exhibitor found")
        browser.close()
        for name in sorted(all_exhibitors):
            print(name)

    return all_exhibitors
