import pytest
import time
from pages.slider_page import ContextPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_alerts(browser):
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    browser.get(url)
    b = ContextPage(browser)
    get_alert = b.move_slider(100, 0)
    #assert get_alert=="You selected a context menu", f"ERROR"