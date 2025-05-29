import time

import pytest
import random
from pages.slider_page import ContextPage
import json


def test_alerts(browser, urls):
    url = urls["horizontal_slider_page"]
    browser.get(url)
    context_page = ContextPage(browser)
    result = context_page.move_slider()
    assert float(result) in (context_page.return_min_and_max_slider()), f"Expected result between 0 and 5, actual result = {result}"
