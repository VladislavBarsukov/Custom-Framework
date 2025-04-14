import pytest
import random
from pages.slider_page import ContextPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_alerts(browser):
    slider_value = random.randint(-55, 55)
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    browser.get(url)
    b = ContextPage(browser)
    result = b.move_slider(slider_value, 0)
    assert 0 <= float(result) <= 5, f"ERROR"
