# pages/textbox_page.py
from locators.textbox_locators import TextBoxLocators

class TextBoxPage:
    def __init__(self, page):
        self.page = page

    def fill_form(self, name, email, address):
        self.page.fill(TextBoxLocators.USERNAME, name)
        self.page.fill(TextBoxLocators.EMAIL, email)
        self.page.fill(TextBoxLocators.CURRENT_ADDRESS, address)
        self.page.fill(TextBoxLocators.PERMANENT_ADDRESS, address)

    def submit_form(self):
        self.page.click(TextBoxLocators.SUBMIT)

    def get_output_name(self):
        return self.page.locator(TextBoxLocators.OUTPUT_NAME).inner_text()
