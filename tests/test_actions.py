import pytest
import random
from pages.slider_page import ContextPage
import enum
from selenium.webdriver.common.keys import Keys
import json


class Directions(str, enum.Enum):
    LEFT_KEY = Keys.ARROW_LEFT
    RIGHT_KEY = Keys.ARROW_RIGHT


def test_alerts(browser):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["horizontal_slider_page"]
    browser.get(url)
    context_page = ContextPage(browser)
    result = context_page.move_slider(random.choice([Directions.LEFT_KEY, Directions.RIGHT_KEY]),
                                      random.randint(0, 5))
    assert 0 <= float(result) <= 5, f"Expected result between 0 and 5, actual result = {result}"
