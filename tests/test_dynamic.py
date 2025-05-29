import pytest
from pages.dynamic_page import DynamicPage
import json


def test_dynamic(browser, urls):
    url = urls["dynamic_page"]
    browser.get(url)
    dynamic_page = DynamicPage(browser)
    dynamic_page.wait_for_open()
    while True:
        browser.refresh()
        img = dynamic_page.get_img()
        if len(set(img)) <= 1:
            break
