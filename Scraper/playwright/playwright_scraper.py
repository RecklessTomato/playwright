from Playwright_simple import scrape_exhibitors as simple_scrape
from Playwright_with_Buttons import scrape_exhibitors as button_scrape


def main():
    # params
    url = "https://www.fierabolzano.it/de/agrialp/ausstellerliste"
    selector = ".card-container"
    card_selector = "div.col-12.exhibitor-container"
    name_selector = "h4.name"
    more_button_selector = "a.btn.btn-default.light.view-more"

    # get the exhibitors
    # exhibitors = simple_scrape(url, selector, card_selector, name_selector)
    exhibitors = button_scrape(url, more_button_selector, card_selector, name_selector)

    print("\n Scraping complete")
    print(f"\n total exhibitors scraped: {len(exhibitors)}")
    for exhibitor in exhibitors:
        print(exhibitor)


if __name__ == "__main__":
    main()
