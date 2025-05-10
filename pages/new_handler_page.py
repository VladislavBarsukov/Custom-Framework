from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.button import Button
from elements.web_element import WebElement


class NewHandlerPage(BasePage):
    NEW_WINDOW_TEXT = "//*[@class='example']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.new_window_text = WebElement(self.browser, self.NEW_WINDOW_TEXT,
                                          description="NewHandlerPage -> Текст New Window")

    def return_text(self):
        return self.new_window_text.get_text()
