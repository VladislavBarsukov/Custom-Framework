import time
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class ContextPage(BasePage):
    FIGURE_BUTTON = 'hot-spot'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.figure_button = Button(self.browser, self.FIGURE_BUTTON,
                               description="ContextPage -> figure button")

    def get_square_alert(self):
        self.figure_button.right_click()
        text = self.browser.get_alert_text()
        self.browser.decline_alert()
        return text