import pytest
from pages.dynamic_page import DynamicPage
import json


def test_dynamic(browser):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["dynamic_page"]
    browser.get(url)
    dynamic_page = DynamicPage(browser)
    while True:
        browser.refresh()
        img = dynamic_page.get_img()
        if len(set(img)) <= 1:
            break
