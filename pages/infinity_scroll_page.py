import time

from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class ScrollPage(BasePage):
    TEXT_ELEMENT = '//*[@class="jscroll-added"]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.text = WebElement(self.browser, self.TEXT_ELEMENT,
                               description="ScrollPage -> text")

    def find_elements(self):
        return self.text.find_elements()
