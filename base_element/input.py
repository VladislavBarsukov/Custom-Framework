from logger.logger import Logger

from base_element.base_element import BaseElement
from selenium.common import WebDriverException


class Input(BaseElement):

    def clear(self):
        element = self.wait_for_visible()
        Logger.info(f"{self}: clear")
        try:
            element.clear()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_clear(self):
        element = self.wait_for_presence()
        Logger.info(f"{self}: js_clear")
        self.browser.execute_script("arguments[0].value = ''", element)

    def send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()
        element = self.wait_for_visible()
        Logger.info(f"{self}: send keys {keys}")
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()
        element = self.wait_for_presence()
        Logger.info(f"{self}: js send keys")
        self.browser.execute_script("arguments[0].value = 'arguments[1]'", element)
