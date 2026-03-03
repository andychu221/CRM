from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        import os
        pwd = os.getcwd()
        page.goto(f"file://{pwd}/index.html")

        # Click the new request card by class
        page.locator(".notebook-card.new-request").click()

        # Wait a moment for UI to switch views
        page.wait_for_timeout(1000)

        # Open the Draft request card
        page.locator("text=Draft").first.click()

        # Wait a moment for the form view to load
        page.wait_for_timeout(1000)

        # Click the dropdown
        page.locator("#btn-purpose-dropdown").click()

        # Click two options (need evaluate to safely click while it overlays)
        page.locator("text=Credit Line Change").nth(1).evaluate("el => el.click()")
        page.locator("text=Payment Term Change").nth(1).evaluate("el => el.click()")

        # Take a final screenshot with the dropdown open to see if it overflows properly and displays multi-select properly
        page.screenshot(path="verification/verification_final3.png")
        print("Final screenshot saved to verification/verification_final3.png")
        browser.close()

if __name__ == "__main__":
    verify()
