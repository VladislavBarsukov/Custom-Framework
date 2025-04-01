from logger.logger import Logger
from operator import truediv
from selenium.webdriver.support import expected_conditions
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebElement

class BaseElement:
    DEFAULT_TIMEOUT = 10

    def __init__(self, browser: Browser,
                 locator: str | tuple,
                 description: str = None,
                 timeout: int = DEFAULT_TIMEOUT):
        self.browser = browser
        self.timeout = timeout
        if isinstance(locator, str):
            if "//" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

        self.description = description if description else str(locator)
        self._wait = WebDriverWait(self.browser.driver, timeout=self.timeout)

    def __str__(self):
        return f"{self.__class__.__name__}{self.description}"

    def __repr__(self):
        return str(self)

    def _wait_for(self, expected_condition):
        try:
            Logger.info(f"{self}: wait_for {expected_condition.__name__}")
            element = self._wait.until(method=expected_condition(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def _wait_for_not(self, expected_condition):
        try:
            Logger.info(f"{self}: wait for not {expected_condition.__name__}")
            self._wait.until_not(method=expected_condition(self.locator))
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_presence(self):
        return self._wait_for(expected_condition=expected_conditions.presence_of_element_located)

    def wait_for_clickable(self):
        return self._wait_for(expected_condition=expected_conditions.element_to_be_clickable)

    def wait_for_visible(self):
        return self._wait_for(expected_condition=expected_conditions.visibility_of_element_located)

    def is_exist(self):
        try:
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def click(self):
        element = self.wait_for_clickable()
        Logger.info(f"{self}: click")
        try:
            element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def right_click(self):
        element = self.wait_for_clickable()
        Logger.info(f"{self}: right_click")
        try:
            action_chains = ActionChains(self.browser.driver)
            action_chains.context_click(element).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_click(self):
        element = self.wait_for_presence()
        Logger.info(f"{self}; js_click")
        self.browser.execute_script("argument[0].click()", element)

    def get_text(self):
        element = self.wait_for_presence()
        Logger.info(f"{self}: get_text")
        try:
            text = element.text
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: text = {text}")
        return text

    def get_attribute(self, name):
        element = self.wait_for_presence()
        Logger.info(f"{self}: get_attribute")
        try:
            value = element.get_attribute(name)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute '{name}' = '{value}'")
        return value

    def get_css_property(self, name):
        element = self.wait_for_presence()
        Logger.info(f"{self}: get_css_property")
        try:
            value = element.value_of_css_property(name)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute '{name}' = '{value}'")
        return value

    def move_slider(self, x=0, y=0):
        element = self.wait_for_clickable()
        Logger.info(f"{self}: move_slider")
        try:
            action = ActionChains(self.browser.driver)
            action.click_and_hold(element).move_by_offset(x, y).perform()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise