from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.web_element import WebElement


class NewHandlerPage(BasePage):
    NEW_WINDOW_TEXT = "//h3[text()='New Window']"

    def __init__(self, browser: Browser):
        super().__init__(browser)

    def return_text(self):
        new_window_text = WebElement(self.browser, self.NEW_WINDOW_TEXT,
                                     description="NewHandlerPage -> Текст New Window")
        text = new_window_text.get_text()
        return text
