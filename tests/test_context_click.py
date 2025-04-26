import pytest
from pages.context_page import ContextPage


def test_alerts(browser):
    url = "https://the-internet.herokuapp.com/context_menu"
    browser.get(url)
    context_page = ContextPage(browser)
    get_alert = context_page.get_square_alert()
    assert get_alert == "You selected a context menu", f"ERROR"
