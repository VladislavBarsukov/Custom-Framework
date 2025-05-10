from logger.logger import Logger
from operator import truediv
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from elements.web_element import WebElement


class MultiWebElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self, browser: Browser,
                 formattable_xpath: str,
                 description: str = None,
                 timeout: int = DEFAULT_TIMEOUT):
        self.index = 1
        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        self.description = description if description else self.formattable_xpath.format("'i'")

    def __iter__(self):
        self.index = 1
        return self

    def __next__(self):
        current_element = WebElement(self.browser,
                                     self.formattable_xpath.format(self.index),
                                     f"{self.description}[{self.index}]",
                                     timeout=self.timeout,
                                     )
        if not current_element.is_exist():
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self):
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self):
        return str(self)
