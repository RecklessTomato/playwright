from Playwright_simple import scrape_exhibitors as simple_scrape
from Playwright_with_Buttons import scrape_exhibitors as button_scrape


def main():
    # params
    url = "https://example.com/scrollseite"
    selector = ".card-container"
    card_selector = ".card"
    name_selector = "h2"
    more_button_selector = "button.load-more"

    simple_scrape(url, selector, card_selector, name_selector)
    # button_scrape(url, more_button_selector, card_selector, name_selector)

    print("\n Scraping complete")


if __name__ == "__main__":
    main()
