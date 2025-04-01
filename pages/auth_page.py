from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class AuthPage(BasePage):
    AFTER_AUTH_ELEMENT = "//*[contains(text(), 'Congratulations! You must have the proper credentials.')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.after_auth_element = WebElement(self.browser, self.AFTER_AUTH_ELEMENT,
                                             description="Page1 -> after_auth_element")

    def is_success_auth(self):
        return self.after_auth_element.wait_for_visible()