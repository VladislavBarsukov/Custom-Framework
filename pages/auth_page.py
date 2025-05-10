from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.web_element import WebElement


class AuthPage(BasePage):
    AFTER_AUTH_ELEMENT = "content"
    AFTER_AUTH_TEXT = "Congratulations! You must have the proper credentials."

    def __init__(self, browser):
        super().__init__(browser)
        self.after_auth_element = WebElement(self.browser, self.AFTER_AUTH_ELEMENT,
                                             description="AuthPage -> after auth element")

    def is_success_auth(self):
        self.after_auth_element.wait_for_visible()
        return self.AFTER_AUTH_TEXT in self.after_auth_element.get_text()
