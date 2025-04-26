import pytest
import random
from pages.slider_page import ContextPage


def test_alerts(browser):
    slider_value = random.randint(-55, 55)
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    browser.get(url)
    context_page = ContextPage(browser)
    result = context_page.move_slider(slider_value, 0)
    assert 0 <= float(result) <= 5, f"ERROR, result not between 0 and 5"
