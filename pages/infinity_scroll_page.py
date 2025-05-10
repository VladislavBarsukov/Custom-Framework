from elements.multi_element import MultiWebElement
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.web_element import WebElement


class ScrollPage(BasePage):
    TEXT_ELEMENTS = '//*[@class="jscroll-inner"]//div[{}]'

    def find_text_elements(self):
        self.texts = MultiWebElement(self.browser, self.TEXT_ELEMENTS,
                                     description=f"img", timeout=0)
        src = [i.get_text() for i in self.texts if len(i.get_text()) > 10]
        return src

    def find_last_element(self):
        self.last_texts = MultiWebElement(self.browser, self.TEXT_ELEMENTS,
                                          description=f"img", timeout=0)
        src = [i for i in self.last_texts if len(i.get_text()) > 10]
        return src[-1]
