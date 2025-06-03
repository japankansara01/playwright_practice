import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        await page.set_viewport_size({"width": 430, "height": 932})
        await page.goto("https://demoqa.com/checkbox")

        # Expand the root to make the checkbox visible
        await page.click('button[title="Toggle"]')  # Expands the "Home" section

        # Now the checkbox is visible and can be checked
        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path="screenshots/checkboxes.png")

        assert await page.is_checked('label[for="tree-node-home"]')
        await expect(page.locator("#result")).to_contain_text("You have selected")

        await context.tracing.stop(path="trace.zip")
        await browser.close()

asyncio.run(main())