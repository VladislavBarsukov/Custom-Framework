from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.button import Button
from elements.web_element import WebElement


class HandlerPage(BasePage):
    CLICK_HERE_ELEMENT = '//*[@href="/windows/new"]'
    UNIQUE_ELEMENT_LOC = "content"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.click_here = Button(self.browser, self.CLICK_HERE_ELEMENT,
                                 description="HandlerPage -> click here button")
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="HandlerPage -> unique element")

    def go_to_new_page(self):
        self.click_here.click()
