from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.web_element import WebElement
from elements.multi_element import MultiWebElement
import itertools


class DynamicPage(BasePage):
    MULTI_IMG = "//*[@class='large-10 columns large-centered']//div[{}]//img"
    UNIQUE_ELEMENT_LOC = "//*[@class='large-10 columns large-centered']//div[3]//img"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="DynamicPage -> unique element")

    def get_img(self):
        self.multi_img = MultiWebElement(self.browser, self.MULTI_IMG,
                                         description="DynamicPage -> get all img", timeout=0)
        src = [i.get_attribute("src") for i in self.multi_img]
        return src
