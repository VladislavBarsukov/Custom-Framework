import time
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class AlertJsPage(BasePage):
    BUTTON_JS_ALERT = '//*[@onclick="jsAlert()"]'
    BUTTON_JS_CONFIRM = '//*[@onclick="jsConfirm()"]'
    BUTTON_JS_PROMPT = '//*[@onclick="jsPrompt()"]'
    RESULT_TEXT = 'result'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.js_alert = Button(self.browser, self.BUTTON_JS_ALERT,
                               description="AlertJsPage -> js_alert")
        self.js_confirm = Button(self.browser, self.BUTTON_JS_CONFIRM,
                                 description="AlertJsPage -> js_confirm")
        self.js_prompt = Button(self.browser, self.BUTTON_JS_PROMPT,
                                description="AlertJsPage -> js_prompt")
        self.result = WebElement(self.browser, self.RESULT_TEXT, description="AlertPage -> result")

    def get_js_alert(self):
        self.js_alert.js_click()
        self.browser.switch_to_alert()
        self.browser.confirm_alert()
        return self.result.get_text()

    def get_js_confirm_ok(self):
        self.js_confirm.js_click()
        self.browser.switch_to_alert()
        self.browser.confirm_alert()
        return self.result.get_text()

    def get_js_confirm_cancel(self):
        self.js_confirm.js_click()
        self.browser.switch_to_alert()
        self.browser.decline_alert()
        return self.result.get_text()

    def get_js_prompt_ok(self, text):
        self.js_prompt.js_click()
        self.browser.switch_to_alert()
        self.browser.send_keys_to_alert(text)
        self.browser.confirm_alert()
        return self.result.get_text()

    def get_js_prompt_cancel(self, text):
        self.js_prompt.js_click()
        self.browser.switch_to_alert()
        self.browser.send_keys_to_alert(text)
        self.browser.decline_alert()
        return self.result.get_text()
