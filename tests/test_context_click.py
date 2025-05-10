import pytest
from pages.context_page import ContextPage
import json


def test_alerts(browser):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["alerts_page"]
    browser.get(url)
    context_page = ContextPage(browser)
    get_alert = context_page.get_square_alert()
    assert get_alert == "You selected a context menu", f"Expected "
