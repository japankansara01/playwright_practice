# from playwright.sync_api import sync_playwright
# import os
#
# def test_all_ui_automation():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context(record_video_dir="../videos")
#         page = context.new_page()
#
#         try:
#             context.tracing.start(screenshots=True, snapshots=True, sources=True)
#
#             # 1️⃣ CHECKBOX & SELECTBOX
#             page.goto("https://demoqa.com/automation-practice-form")
#             page.check("label[for='hobbies-checkbox-1']")
#
#             # Custom dropdown for state
#             page.click("#state")  # open dropdown
#             page.click("div[id^='react-select'][id*='option-0']")  # select NCR
#
#             # Custom dropdown for city
#             page.click("#city")  # open dropdown
#             page.click("div[id^='react-select'][id*='option-0']")  # select Delhi
#
#             # 2️⃣ MOUSE EVENTS
#             page.goto("https://demoqa.com/buttons")
#             page.dblclick("#doubleClickBtn")
#             page.click("#rightClickBtn", button="right")
#             page.hover("button.btn-primary")
#
#             # 3️⃣ FILE UPLOAD & DOWNLOAD
#             page.goto("https://demoqa.com/upload-download")
#             file_path = os.path.abspath("sample.txt")
#             with open("sample.txt", "w") as f: f.write("Hello Harsh QA")
#             page.set_input_files("#uploadFile", file_path)
#
#             with page.expect_download() as download_info:
#                 page.click("#downloadButton")
#             download = download_info.value
#             download.save_as("downloads/DownloadedFile.png")
#
#             # 4️⃣ SVG ELEMENT HANDLING (demo only)
#             print("SVG: [Demo only — no direct SVG interaction on this site]")
#
#             # 5️⃣ JAVASCRIPT EXECUTION
#             page.goto("https://demoqa.com/text-box")
#             page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#             count = page.evaluate("() => document.querySelectorAll('input').length")
#             print("JS Eval: Number of input fields:", count)
#
#             # 7️⃣ ASSERTIONS
#             page.fill("#userName", "Harsh QA")
#             page.fill("#userEmail", "harsh@test.com")
#             page.fill("#currentAddress", "India")
#             page.click("#submit")
#             output_name = page.locator("#output #name").inner_text()
#             assert "Harsh QA" in output_name, "Name not submitted properly"
#
#             # 8️⃣ SCREENSHOT (success)
#             page.screenshot(path="screenshots/final_page.png")
#             print("✅ Test completed successfully")
#
#         except Exception as e:
#             page.screenshot(path="screenshots/error.png")
#             print("❌ Test failed, screenshot saved.")
#             raise e
#
#         finally:
#             # ✅ Stop and export trace
#             context.tracing.stop(path="trace.zip")
#             context.close()
#             browser.close()