from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.web_element import WebElement
from elements.multi_element import MultiWebElement
import itertools


class DynamicPage(BasePage):
    MULTI_IMG = "//*[@class='large-10 columns large-centered']//div[{}]//img"

    def get_img(self):
        self.multi_img = MultiWebElement(self.browser, self.MULTI_IMG,
                                         description=f"img", timeout=0)
        src = [i.get_attribute("src") for i in self.multi_img]
        return src
