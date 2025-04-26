import pytest
from pages.infinity_scroll_page import ScrollPage


def test_scroll(browser):
    url = "https://the-internet.herokuapp.com/infinite_scroll"
    browser.get(url)
    scroll_page = ScrollPage(browser)
    g = 0
    h = []
    while g != 27:
        browser.scroll_down(200)
        i = scroll_page.find_elements()
        if i not in h:
            h.append(i)
            g = len(h)
    assert len(h) == 27, "ERROR, find not enough or too much elements"
