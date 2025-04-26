import pytest
from pages.dynamic_page import DynamicPage


def test_dynamic(browser):
    url = "https://the-internet.herokuapp.com/dynamic_content"
    browser.get(url)
    dynamic_page = DynamicPage(browser)

    while True:
        browser.refresh()
        img_1 = dynamic_page.get_img1()
        img_2 = dynamic_page.get_img2()
        img_3 = dynamic_page.get_img3()
        if img_1 == img_2 and img_2 == img_3 and img_1 == img_3:
            break
