from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class ContextPage(BasePage):
    SLIDER_ELEMENT = '//*[@type="range"]'
    RESULT_SLIDER = 'range'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.slider = WebElement(self.browser, self.SLIDER_ELEMENT,
                                 description="ContextPage -> figure button")
        self.result = WebElement(self.browser, self.RESULT_SLIDER,
                                 description="ContextPage -> figure button")

    def move_slider(self, x, y=0):
        self.slider.move_slider(x, y)
        return self.result.get_text()
