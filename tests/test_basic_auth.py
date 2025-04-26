import pytest
from pages.auth_page import AuthPage


def test_basic_auth(browser):
    expected_text = "Congratulations! You must have the proper credentials."
    username = "admin"
    password = "admin"
    base_url = "the-internet.herokuapp.com/basic_auth"
    url = f"https://{username}:{password}@{base_url}"
    browser.get(url)
    auth_page = AuthPage(browser)
    element = auth_page.is_success_auth()
    assert element.text == expected_text, f"Expected {expected_text}, get {element.text}"
