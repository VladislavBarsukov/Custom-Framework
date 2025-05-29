from elements.multi_element import MultiWebElement
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.web_element import WebElement


class ScrollPage(BasePage):
    TEXT_ELEMENTS = '//*[@class="jscroll-inner"]//div[{}]'
    LOADING_TEXT = ('', 'Loading...')

    def find_text_elements(self):
        self.texts = MultiWebElement(self.browser, self.TEXT_ELEMENTS,
                                     description=f"find text elements", timeout=0)

        src = [i.get_text() for i in self.texts if i.get_text() not in self.LOADING_TEXT]
        return src

    def scroll_to_last_element(self):
        self.last_texts = MultiWebElement(self.browser, self.TEXT_ELEMENTS,
                                          description=f"scroll to last element", timeout=0)
        src = [i for i in self.last_texts if i.get_text() not in self.LOADING_TEXT]
        src[-1].scroll_into_view()
