from Playwright_simple import scrape_exhibitors as simple_scrape
from Playwright_with_Buttons import scrape_exhibitors as button_scrape


def main():
    # params
    url1 = "https://example.com/scrollseite"
    selector = ".card-container"
    card_selector1 = ".card"
    name_selector1 = "h2"
    more_button_selector = "button.load-more"


    simple_scrape(url1, selector1, card_selector1, name_selector1)

    print("\n" + "-" * 40 + "\n")

    # Beispiel 2: Seite mit "Mehr anzeigen"
    url2 = "https://example.com/buttonseite"
    more_button_selector = "button.load-more"  # "Mehr anzeigen"-Button
    card_selector2 = ".exhibitor-card"
    name_selector2 = "h2"

    button_scrape(url2, more_button_selector, card_selector2, name_selector2)

    print("\n✅ Scraping abgeschlossen!")


if __name__ == "__main__":
    main()
