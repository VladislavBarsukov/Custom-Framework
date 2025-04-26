import logging

from selenium.common import WebDriverException
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from logger.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 100

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)
        self.main_handle = None
        self._wait = WebDriverWait(self._driver, self.DEFAULT_TIMEOUT)

    @property
    def driver(self):
        return self._driver

    def get(self, url: str):
        Logger.info(f'{self} get {url}')
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def close(self):
        Logger.info(f"{self}: close window handle = {self._driver.current_window_handle}")
        self._driver.close()

    def quit(self):
        Logger.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def execute_script(self, script: str, *args):
        Logger.info(f"{self}: execute script = '{script}' with args {args}")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def save_screenshot(self):
        Logger.info(f"{self}: save screenshot {filename}")
        self._driver.save_screenshot(filename=filename)

    def refresh(self):
        Logger.info(f"{self} refresh")
        self._driver.refresh()

    def switch_to_default_window(self):
        Logger.info(f"{self} switch_to_default_window")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_default_content(self):
        Logger.info(f"{self} switch_to_default_content")
        self._driver.switch_to.default_content()

    def switch_to_window(self, window_handle):
        Logger.info(f"{self} switch to window {window_handle}")
        self._driver.switch_to.window(window_handle)
        self.main_handle = window_handle

    def switch_to_windows(self, num: int):
        Logger.info(f"{self} switch to window {num}")
        switch = self._driver.window_handles[num]
        self._driver.switch_to.window(switch)
        self.main_handle = switch

    def make_dump(self):
        Logger.info(f"{self}: make_dump")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dump_{timestamp}.png"
        filepath = os.path.join("dumps", filename)
        if not os.path.exists("dumps"):
            os.makedirs("dumps")
        self._driver.save_screenshot(filepath)

    def switch_to_iframe(self, frame):
        Logger.info(f"{self}: switch_to_iframe")
        return self._driver.switch_to.frame(frame.wait_for_presence())

    def wait_alert_present(self):
        Logger.info(f"{self} wait_alert_present")
        return self._wait.until(expected_conditions.alert_is_present())

    def switch_to_alert(self):
        Logger.info(f"{self} switch to alert")
        self.wait_alert_present()
        return self._driver.switch_to.alert

    def get_alert_text(self):
        Logger.info(f"{self} get alert text")
        return self.switch_to_alert().text

    def confirm_alert(self):
        Logger.info(f"{self} confirm alert")
        self.switch_to_alert().accept()

    def decline_alert(self):
        Logger.info(f"{self} decline alert")
        self.switch_to_alert().dismiss()

    def send_keys_to_alert(self, text):
        Logger.info(f"{self} send_keys_to_alert: sending '{text}'")
        alert = self.switch_to_alert()
        alert.send_keys(text)
        Logger.info("Text sent to alert successfully.")

    def go_back(self):
        Logger.info(f"{self}: go back to previous page")
        try:
            self._driver.back()
        except WebDriverException as err:
            Logger.error(f"{self}: Error navigating back: {err}")
            raise

    def scroll_down(self, scroll_distance):
        Logger.info(f"{self}: scroll_down")
        js = f"window.scrollBy(0, {scroll_distance});"
        self._driver.execute_script(js)

    def __str__(self):
        return f"{self.__class__.__name__}{self._driver.session_id}"

    def __repr__(self):
        return str(self)
