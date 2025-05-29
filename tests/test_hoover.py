import json
import pytest
from pages.hoover_page import HooverPage


def test_hoover(browser, urls):
    USER_URL = "https://the-internet.herokuapp.com/users/"
    url = urls["hoover_page"]
    browser.get(url)
    hoover_page = HooverPage(browser)
    for i in range(1, 4):
        user_name = hoover_page.move_to(i)
        assert user_name == f"name: user{i}", f"Expect user{i}, get {user_name}"
        hoover_page.go_to_user_url(i)
        current_url = browser.driver.current_url
        assert current_url == f"{USER_URL}{i}", f"{USER_URL}{i}, get {current_url}"
        browser.go_back()
