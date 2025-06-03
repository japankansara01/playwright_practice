import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("search_term,expected_heading", [
    ("Quality Assurance", "Quality assurance")  # Wikipedia capitalizes only first word
])
def test_wikipedia_search(page: Page, search_term, expected_heading):
    # Go to Wikipedia
    page.goto("https://www.wikipedia.org")

    # Type in the search box
    page.fill("input[name='search']", search_term)

    # Click the search button
    page.click("button[type='submit']")

    # Wait and verify the heading
    heading = page.inner_text("h1")
    assert heading == expected_heading, f"Expected heading to be '{expected_heading}' but got '{heading}'"