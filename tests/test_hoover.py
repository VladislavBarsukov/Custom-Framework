import json
import pytest
from pages.hoover_page import HooverPage


def test_hoover(browser):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["hoover_page"]
    browser.get(url)
    hoover_page = HooverPage(browser)
    for i in range(1, 4):
        user_name = hoover_page.move_to(i)
        assert user_name == f"name: user{i}", f"Expect user{i}, get {user_name}"
        user_url = hoover_page.go_to_user_url(i)
        assert user_url == f"https://the-internet.herokuapp.com/users/{i}", f"Expect https://the-internet.herokuapp.com/users/1{i}, get {user_url}"
        browser.go_back()
