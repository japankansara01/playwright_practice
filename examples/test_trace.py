# from playwright.sync_api import sync_playwright
#
# def test_with_trace():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#
#         # Start tracing before creating the page
#         context.tracing.start(screenshots=True, snapshots=True, sources=True)
#
#         page = context.new_page()
#         page.goto("https://example.com")
#         page.click("text=More information")
#         page.pause()
#         # page.wait_for_timeout(5000)
#
#         # Stop tracing and export it to a zip file
#         context.tracing.stop(path="trace.zip")
#         browser.close()