from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement


class IframePage(BasePage):
    NESTED_FRAMES_BUTTON = "//span[text()='Nested Frames']"
    PARENT_FRAME_LOCATOR = "frame1"
    CHILD_FRAME_LOCATOR = '//*[contains(@srcdoc, "<p>Child Iframe</p>")]'
    PARENT_TEXT = "//*[contains(text(), 'Parent frame')]"
    CHILD_TEXT = "//*[contains(text(), 'Child Iframe')]"
    FRAMES = "//span[text()='Frames']"
    SAMPLE_PAGE_TEXT = "sampleHeading"
    BIG_FRAME = "frame1"
    SMALL_FRAME = "frame2"
    BIG_FRAME_TEXT_BY_ID = "sampleHeading"
    SMALL_FRAME_TEXT_BY_ID = "sampleHeading"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.nested_frames_button = Button(self.browser, self.NESTED_FRAMES_BUTTON,
                                           description="IframePage -> nested_frames_button")
        self.parent_frame_element = WebElement(self.browser, self.PARENT_FRAME_LOCATOR,
                                               description="IframePage -> parent_frame_element")
        self.big_frame_text_element = WebElement(self.browser, self.BIG_FRAME_TEXT_BY_ID,
                                                 description="IframePage -> big_frame_text_element")
        self.big_frame_element = WebElement(self.browser, self.BIG_FRAME, description="IframePage -> big_frame_element")
        self.small_frame_text_element = WebElement(self.browser, self.SMALL_FRAME_TEXT_BY_ID,
                                                   description="IframePage -> small_frame_text_element")
        self.small_frame_element = WebElement(self.browser, self.SMALL_FRAME,
                                              description="IframePage -> small_frame_element")
        self.frame_parent_element = WebElement(self.browser, self.PARENT_TEXT,
                                               description="IframePage -> frame_parent_element")
        self.frame_parent_element = WebElement(self.browser, self.PARENT_TEXT,
                                               description="IframePage -> frame_parent_element")
        self.child_frame_element = WebElement(self.browser, self.CHILD_FRAME_LOCATOR,
                                              description="IframePage -> child_frame_element")
        self.frame_child_element = WebElement(self.browser, self.CHILD_TEXT,
                                              description="IframePage -> frame_child_element")
        self.frames = WebElement(self.browser, self.FRAMES, description="IframePage -> frames")

    def open_alerts_frame_windows(self):
        self.alerts_frame_windows_button.click()

    def open_nested_frames(self):
        self.nested_frames_button.click()

    def open_frames(self):
        self.frames.click()

    def switch_and_get_parent_nested_frames_text(self):
        self.browser.switch_to_iframe(self.parent_frame_element)
        frame_parent_text = self.frame_parent_element.get_text()
        self.browser.switch_to_default_content()
        return frame_parent_text

    def switch_and_get_child_nested_frames_text(self):
        self.browser.switch_to_iframe(self.parent_frame_element)
        self.browser.switch_to_iframe(self.child_frame_element)
        frame_child_text = self.frame_child_element.get_text()
        self.browser.switch_to_default_content()
        return frame_child_text

    def switch_and_get_big_frames_text(self):
        self.browser.switch_to_iframe(self.big_frame_element)
        text = self.big_frame_text_element.get_text()
        self.browser.switch_to_default_content()
        return text

    def switch_and_get_small_frames_text(self):
        self.browser.switch_to_iframe(self.small_frame_element)
        text = self.small_frame_text_element.get_text()
        self.browser.switch_to_default_content()
        return text
