from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement


class MainFramePage(BasePage):
    ALERTS_FRAME_AND_WINDOWS = '//*[contains(text(),"Alerts, Frame & Windows")]'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.alerts_frame_windows_button = Button(self.browser, self.ALERTS_FRAME_AND_WINDOWS,
                                                  description="IframePage -> alerts_frame_windows_button")

    def open_alerts_frame_windows(self):
        self.alerts_frame_windows_button.click()
