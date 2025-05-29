import pytest
from pages.handler_page import HandlerPage
from pages.new_handler_page import NewHandlerPage


def test_handlers(browser, urls):
    url = urls["handler_page"]
    browser.get(url)
    handler_page_1 = HandlerPage(browser)
    handler_page_1.wait_for_open()
    handler_page_1.go_to_new_page()
    browser.switch_to_window('New Window')
    handler_page_2 = NewHandlerPage(browser)
    handler_page_2.wait_for_open()
    text1 = handler_page_2.return_text()
    assert text1 == "New Window", f"Expect text 'New Window', get {text1}"
    browser.switch_to_default_window()
    handler_page_1.go_to_new_page()
    handler_page_3 = NewHandlerPage(browser)
    handler_page_3.wait_for_open()
    browser.switch_to_window('New Window')
    text2 = handler_page_3.return_text()
    assert text2 == "New Window", f"Expect text 'New Window', get {text2}"
    browser.switch_to_default_window()
    browser.switch_to_window('New Window')
    browser.close()
    browser.switch_to_window('New Window')
    browser.close()
