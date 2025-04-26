import pytest
from pages.handler_page import HandlerPage
from pages.new_handler_page import NewHandlerPage


def test_handlers(browser):
    url = "https://the-internet.herokuapp.com/windows"
    browser.get(url)
    handler_page_1 = HandlerPage(browser)
    handler_page_1.go_to_new_page()
    handler_page_2 = NewHandlerPage(browser)
    text1 = handler_page_2.return_text()
    assert text1 == "New Window", "Error"
    handler_page_1.switch_to_original_window()
    handler_page_1.go_to_new_page()
    handler_page_3 = NewHandlerPage(browser)
    text2 = handler_page_3.return_text()
    assert text2 == "New Window", "Error"
    handler_page_1.switch_to_original_window()
    browser.switch_to_windows(1)
    browser.close()
    browser.switch_to_windows(1)
    browser.close()
