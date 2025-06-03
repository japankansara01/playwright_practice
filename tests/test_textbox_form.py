import pytest
from pages.textbox_page import TextBoxPage


def test_fill_textbox_form(page):
    page.goto("https://demoqa.com/text-box")
    textbox = TextBoxPage(page)

    textbox.fill_form("Harsh QA", "harsh@example.com", "India")
    textbox.submit_form()

    assert "Harsh QA" in textbox.get_output_name()
