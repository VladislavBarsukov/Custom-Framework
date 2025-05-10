from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.input import Input
from elements.web_element import WebElement


class ContextPage(BasePage):
    SLIDER_ELEMENT = '//*[@type="range"]'
    RESULT_SLIDER = 'range'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.slider = Input(self.browser, self.SLIDER_ELEMENT,
                            description="ContextPage -> figure button")
        self.result = WebElement(self.browser, self.RESULT_SLIDER,
                                 description="ContextPage -> figure button")

    def move_slider(self, key, count):
        self.slider.click()
        for i in range(count):
            self.slider.send_keys(key, False)
        return self.result.get_text()
