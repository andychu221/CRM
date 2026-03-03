from playwright.sync_api import sync_playwright
import os

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
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

        # Wait for the dropdown content
        page.wait_for_timeout(500)

        # Click options
        page.locator(".dropdown-item-check").filter(has_text="Others").first.click()
        page.locator(".dropdown-item-check").filter(has_text="New Credit Line").first.click()

        # Hide the dropdown by clicking somewhere else so we can see the input
        page.locator("text=Request Purpose").first.click()

        # Take a final screenshot
        page.screenshot(path="verification/verification_others4.png")
        print("Final screenshot saved to verification/verification_others4.png")
        browser.close()

if __name__ == "__main__":
    verify()
