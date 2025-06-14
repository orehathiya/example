from playwright.sync_api import Page, expect


def test_home_page(page: Page) -> None:
    """Test the home page returns the expected JSON."""
    page.goto("http://localhost:5001")
    expect(page.locator("body")).to_contain_text("Hello, World")
