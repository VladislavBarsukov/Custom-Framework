import pytest
from pages.auth_page import AuthPage
import json
import time


@pytest.mark.parametrize("username, password", [('admin', 'admin')])
def test_basic_auth(browser, urls, username, password):
    base_url = urls["basic_auth_page"]
    url = f"https://{username}:{password}@{base_url}"
    browser.get(url)
    auth_page = AuthPage(browser)
    element = auth_page.is_success_auth()
    assert 'Congratulations! You must have the proper credentials.' in element, f"Expected 'Congratulations! You must have the proper credentials.' in {element}, but not"
