import time

import pytest
from pages.dynamic_page import DynamicPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_dynamic(browser):
    url = "https://the-internet.herokuapp.com/dynamic_content"
    q = browser
    q.get(url)
    a=DynamicPage(browser)

    while True:
        browser.refresh()
        q = a.get_img1()
        w = a.get_img2()
        e = a.get_img3()
        if q == w and w == e and q == e:
            print("------------------------------------------------------------")
            print(q)
            print(w)
            print(e)
            print("------------------------------------------------------------")
            break
