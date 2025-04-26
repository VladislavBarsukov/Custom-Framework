from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class HooverPage(BasePage):
    def __init__(self, browser: Browser, user_num):
        super().__init__(browser)
        self.user_num = user_num
        self.user = WebElement(self.browser, f"(//*[@class='figure'])[{self.user_num}]",
                               description="HooverPage -> user element")
        self.user_name = WebElement(self.browser, f"//*[contains(text(), 'name: user{self.user_num}')]",
                                    description="HooverPage -> user name")
        self.user_url = WebElement(self.browser, f"(//*[@href='/users/{self.user_num}'])",
                                   description="HooverPage -> user url")

    def move_to(self):
        self.user.move_to_element()
        return self.user_name.get_text()

    def go_to_user_url(self):
        self.user_url.click()
