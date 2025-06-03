# import pytest
# from playwright.sync_api import sync_playwright
#
# def test_demoqa_all_in_one():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#
#         # Visit site with form
#         page.goto("https://demoqa.com/text-box")
#
#         # 1️⃣ LOCATOR with labels
#         page.locator("#userName").fill("Harsh QA")
#         page.locator("#userEmail").fill("harsh@test@qa.com")
#
#         # 2️⃣ XPATH with contains()
#         # Fill current address using partial text match
#         page.locator("xpath=//textarea[contains(@id,'currentAddress')]").fill("Gujarat, India")
#
#         # 3️⃣ CSS SELECTOR for button
#        # Click submit using class
#         page.locator("button.btn-primary").click()
#
#         # 4️⃣ XPATH AXES — get label before email input
#         email_label = page.locator("xpath=//input[@id='userEmail']/preceding::label[1]").inner_text()
#         print("Label before Email field:", email_label)
#
#         page.goto("https://demoqa.com/alerts")
#
#         # 5️⃣ ALERT Handling
#         def handle_dialog(dialog):
#             print("✅ Alert Text:", dialog.message)
#             dialog.accept()
#
#         page.once("dialog", handle_dialog)
#         page.click("#alertButton")  # Triggers JS alert
#
#         print("✅ Test run completed.")
#         browser.close()