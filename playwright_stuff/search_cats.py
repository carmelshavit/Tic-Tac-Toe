from playwright.sync_api import sync_playwright


def search_cats():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True if you don't want to see the browser

        page = browser.new_page()

        # Go to Google's homepage
        page.goto("https://www.google.com")

        # Find the search box and type "cats"
        page.fill('textarea[name="q"]', "cats")

        # Press Enter to perform the search
        page.press('textarea[name="q"]', "Enter")

        # Wait for the results page to load
        page.wait_for_load_state('load')

        # Optionally, you can print the titles of the search results
        titles = page.query_selector_all('h3')
        for i, title in enumerate(titles):
            print(f"Result {i + 1}: {title.inner_text()}")

        # Close the browser
        browser.close()


if __name__ == "__main__":
    search_cats()
