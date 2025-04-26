import time

import pytest
from pages.hoover_page import HooverPage


def test_hoover(browser):
    url = "https://the-internet.herokuapp.com/hovers"
    browser.get(url)
    for i in range(1, 4):
        hoover_page = HooverPage(browser, i)
        user_name = hoover_page.move_to()
        assert user_name == f"name: user{hoover_page.user_num}", f"ERROR"
        hoover_page.go_to_user_url()
        browser.go_back()
