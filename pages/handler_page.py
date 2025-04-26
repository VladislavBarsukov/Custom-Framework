from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.web_element import WebElement


class HandlerPage(BasePage):
    CLICK_HERE_ELEMENT = '//*[@href="/windows/new"]'
    NEW_WINDOW_TEXT = "//h3[text()='New Window']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.click_here = Button(self.browser, self.CLICK_HERE_ELEMENT,
                                 description="HandlerPage -> click here button")
        self.original_window = self.browser._driver.current_window_handle

    def go_to_new_page(self):
        self.click_here.click()
        new_window_handle = \
            [handle for handle in self.browser._driver.window_handles if handle != self.browser.main_handle][0]
        self.browser.switch_to_window(new_window_handle)

    def switch_to_original_window(self):
        self.browser.switch_to_window(self.original_window)
