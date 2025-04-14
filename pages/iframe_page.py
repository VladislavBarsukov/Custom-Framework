from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement


class IframePage(BasePage):
    NESTED_FRAMES_BUTTON = "//span[text()='Nested Frames']"
    ALERTS_FRAME_AND_WINDOWS = '//*[contains(text(),"Alerts, Frame & Windows")]'
    PARENT_FRAME_LOCATOR = "frame1"
    CHILD_FRAME_LOCATOR = '//*[contains(@srcdoc, "<p>Child Iframe</p>")]'
    PARENT_TEXT = "//*[contains(text(), 'Parent frame')]"
    CHILD_TEXT = "//*[contains(text(), 'Child Iframe')]"
    FRAMES = "//span[text()='Frames']"
    SAMPLE_PAGE_TEXT = "sampleHeading"
    BIG_FRAME = "frame1"
    SMALL_FRAME = "frame2"
    BIG_FRAME_TEXT = "sampleHeading"
    SMALL_FRAME_TEXT = "sampleHeading"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.nested_frames_button = Button(self.browser, self.NESTED_FRAMES_BUTTON,
                               description="self.nested_frames_button")
        self.alerts_frame_windows_button = Button(self.browser, self.ALERTS_FRAME_AND_WINDOWS,
                                    description="self.alerts_frame_windows_button")
        self.parent_frame_element = WebElement(self.browser, self.PARENT_FRAME_LOCATOR,
                                                    description="self.parent_frame_element")

    def open_alerts_frame_windows(self):
        self.alerts_frame_windows_button.click()

    def open_nested_frames(self):
        self.nested_frames_button.click()

    def switch_to_default(self):
        self.browser.switch_to_default_content()

    def open_frames(self):
        self.frames = WebElement(self.browser, self.FRAMES, description="self.frames")
        self.frames.click()

    def switch_and_check_big_frames_text(self):
        self.big_frame_element = WebElement(self.browser, self.BIG_FRAME, description="self.big_frame_element")
        self.browser.switch_to_iframe(self.big_frame_element)
        self.big_frame_text_element = WebElement(self.browser, self.BIG_FRAME_TEXT, description="self.big_frame_element")
        text = self.big_frame_text_element.get_text()
        return text

    def switch_and_check_small_frames_text(self):
        self.small_frame_element = WebElement(self.browser, self.SMALL_FRAME, description="self.small_frame_element")
        self.browser.switch_to_iframe(self.small_frame_element)
        self.small_frame_text_element = WebElement(self.browser, self.SMALL_FRAME_TEXT,description="self.big_frame_element")
        text = self.small_frame_text_element.get_text()
        return text

    def switch_and_check_parent_nested_frames_text(self):
        self.browser.switch_to_iframe(self.parent_frame_element)
        self.frame_parent_element = WebElement(self.browser, self.PARENT_TEXT, description="self.frame_parent_element")
        self.child_frame_element = WebElement(self.browser, self.CHILD_FRAME_LOCATOR,
                                              description="self.child_frame_element")
        frame_parent_text = self.frame_parent_element.get_text()
        return frame_parent_text

    def switch_and_check_child_nested_frames_text(self):
        self.browser.switch_to_iframe(self.child_frame_element)
        self.frame_child_element = WebElement(self.browser, self.CHILD_TEXT, description="self.frame_child_element")
        frame_child_text = self.frame_child_element.get_text()
        return frame_child_text