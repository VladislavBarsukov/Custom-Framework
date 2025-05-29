from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement


class HooverPage(BasePage):
    USER_ELEMENT_LOCATOR = "(//*[@class='figure'])[{}]"
    USER_NAME_LOCATOR = "//*[contains(text(), 'name: user{}')]"
    USER_URL_LOCATOR = "(//*[@href='/users/{}'])"

    def move_to(self, num):
        self.user = WebElement(self.browser, self.USER_ELEMENT_LOCATOR.format(num),
                               description="HooverPage -> user element")
        self.user_name = WebElement(self.browser, self.USER_NAME_LOCATOR.format(num),
                                    description="HooverPage -> user name")
        self.user.move_to_element()
        return self.user_name.get_text()

    def go_to_user_url(self, num):
        self.user_url = WebElement(self.browser, self.USER_URL_LOCATOR.format(num),
                                   description="HooverPage -> user url")
        self.user_url.click()
