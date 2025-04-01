import pytest
from pages.context_page import ContextPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_alerts(browser):
    url = "https://the-internet.herokuapp.com/context_menu"
    browser.get(url)
    b = ContextPage(browser)
    get_alert = b.get_square_alert()
    assert get_alert=="You selected a context menu", f"ERROR"