import time

from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class DynamicPage(BasePage):
    IMG_1 = '//*[@id="content"]/div[1]/div[1]/img'
    IMG_2 = '//*[@id="content"]/div[2]/div[1]/img'
    IMG_3 = '//*[@id="content"]/div[3]/div[1]/img'

    def __init__(self, browser: Browser):
        super().__init__(browser)

    def get_img1(self):
        self.img_1 = WebElement(self.browser, self.IMG_1,
                                description="img_1")
        text = self.img_1.get_src()
        return text

    def get_img2(self):
        self.img_2 = WebElement(self.browser, self.IMG_2,
                                description="img_2")
        text = self.img_2.get_src()
        return text

    def get_img3(self):
        self.img_3 = WebElement(self.browser, self.IMG_3,
                                description="img_3")
        text = self.img_3.get_src()
        return text
