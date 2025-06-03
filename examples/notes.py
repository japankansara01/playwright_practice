import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.get_by_text("Radio Button").click()
    page.get_by_text("Yes").click()
    page.get_by_text("Impressive").click()
    page.get_by_text("Buttons").click()
    page.get_by_role("button", name="Click Me", exact=True).click()
    page.get_by_text("Interactions").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)