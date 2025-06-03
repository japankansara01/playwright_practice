import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        await page.set_viewport_size({"width": 1024, "height": 1366})
        await page.goto("https://demoqa.com/buttons")

        button = page.locator("text=Click Me").nth(2)
        await button.click()
        await page.screenshot(path="screenshots/dynamicClick.png")

        # Assertion
        await expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")

        # --- Double Click ---
        button = page.locator("text=Click Me").nth(0)
        await button.dblclick()
        await page.screenshot(path="screenshots/doubleClick.png")

        # Assertion
        await expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")

        # --- Right Click ---
        # Optional: Un-comment to enable right click behavior test
        button = page.locator("text=Click Me").nth(1)
        await button.click(button="right")
        await page.screenshot(path="screenshots/rightClick.png")
        await expect(page.locator("#rightClickMessage")).to_have_text("You have done a right click")

        await context.tracing.stop(path="trace.zip")
        await browser.close()

asyncio.run(main())