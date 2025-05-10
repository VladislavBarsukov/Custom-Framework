import pytest
from pages.auth_page import AuthPage
import json


def test_basic_auth(browser):
    username = "admin"
    password = "admin"
    with open("urls.json", "r") as f:
        urls = json.load(f)
    base_url = urls["basic_auth_page"]
    url = f"https://{username}:{password}@{base_url}"
    browser.get(url)
    auth_page = AuthPage(browser)
    element = auth_page.is_success_auth()
    assert element == True, f"Expected {element} = True, get False"
