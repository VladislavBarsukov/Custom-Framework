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
        self.main_handle = self._driver.current_window_handle  # уникальный идентификатор активного окна браузера

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
        Logger.info(f"{self} switch")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_window(self, title: str):
        Logger.info(f"{self} switch to window {title}")
        self._driver.switch_to.window(title)
        if self._driver.title == title:
            self.main_handle = self._driver.current_window_handle
            Logger.info(f"{self}: now main_handle is {self.main_handle}")
        else:
            Logger.error(f"Wasn't found page with title {title}")
            raise ValueError(f"Wasn't found page with title {title}")

    def make_dump(self):
        Logger.info(f"{self}: make_dump")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dump_{timestamp}.png"
        filepath = os.path.join("dumps", filename)
        if not os.path.exists("dumps"):
            os.makedirs("dumps")
        self._driver.save_screenshot(filepath)

    #def switch_to_iframe(self, frame: BaseElement):
    #    Logger.info(f"{self}: switch_to_iframe")
    #    return self._driver.switch_to.frame(frame.wait_for_presense)

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
        try:
            self.switch_to_alert().accept()
        except NoAlertPresentException:
            Logger.warning("No alert was present when trying to confirm.")
        except TimeoutException:
            Logger.warning("Alert did not appear within the expected time.")

    def decline_alert(self):
        Logger.info(f"{self} decline alert")
        try:
            self.switch_to_alert().dismiss()
        except NoAlertPresentException:
            Logger.warning("No alert was present when trying to confirm.")
        except TimeoutException:
            Logger.warning("Alert did not appear within the expected time.")

    def send_keys_to_alert(self, text):
        Logger.info(f"{self} send_keys_to_alert: sending '{text}'")
        try:
            alert = self.switch_to_alert()
            alert.send_keys(text)
            Logger.info("Text sent to alert successfully.")
        except NoAlertPresentException:
            Logger.warning("No alert was present when trying to send keys.")
        except TimeoutException:
            Logger.warning("Alert did not appear within the expected time.")

    def __str__(self):
        return f"{self.__class__.__name__}{self._driver.session_id}"

    def __repr__(self):
        return str(self)
