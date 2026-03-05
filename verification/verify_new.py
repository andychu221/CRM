from playwright.sync_api import sync_playwright
import os

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        pwd = os.getcwd()
        page.goto(f"file://{pwd}/index.html")
        page.wait_for_timeout(1000)

        # Click the 'New Request' card
        page.click("text=New Request")
        page.wait_for_timeout(500)

        # Now click the new draft card that got created
        page.click("text=REQ-2025-4")
        page.wait_for_timeout(1000)

        # Take a screenshot to verify empty new request behavior
        page.screenshot(path="verification/verification_new_req_detail.png")
        print("Final screenshot saved to verification/verification_new_req_detail.png")

        browser.close()

if __name__ == "__main__":
    verify()
