import pytest
from pages.hoover_page import HooverPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_hoover(browser):
    url = "https://the-internet.herokuapp.com/hovers"
    browser.get(url)
    for i in range(1, 4):
        b = HooverPage(browser, i)
        user_name = b.move_to()
        assert user_name==f"name: user{b.user_num}", f"ERROR"
        b.go_to_user_url()
        browser.go_back()