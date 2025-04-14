import time

import pytest
from pages.handler_page import HandlerPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_handlers(browser):
    url = "https://the-internet.herokuapp.com/windows"
    q = browser
    q.get(url)
    a = HandlerPage(browser)
    a.go_to_new_page()
    text1 = a.return_text()
    assert text1=="New Window", "Error"
    a.go_to_new_page()
    text2 = a.return_text()
    assert text2 == "New Window", "Error"
    q.switch_to_windows(1)
    q.close()
    q.switch_to_windows(1)
    q.close()
