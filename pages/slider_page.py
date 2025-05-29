from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from elements.input import Input
from elements.web_element import WebElement
from selenium.webdriver.common.keys import Keys
import enum
import random


class Directions(str, enum.Enum):
    LEFT_KEY = Keys.ARROW_LEFT
    RIGHT_KEY = Keys.ARROW_RIGHT


class ContextPage(BasePage):
    SLIDER_ELEMENT = '//*[@type="range"]'
    RESULT_SLIDER = 'range'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.slider = Input(self.browser, self.SLIDER_ELEMENT,
                            description="ContextPage -> figure button")
        self.result = WebElement(self.browser, self.RESULT_SLIDER,
                                 description="ContextPage -> figure button")

    def move_slider(self):
        MAX_SLIDER = float(self.slider.get_attribute("max"))
        MIN_SLIDER = float(self.slider.get_attribute("min"))
        STEP_SLIDER = float(self.slider.get_attribute("step"))
        DIRECTION = random.choice([Directions.LEFT_KEY, Directions.RIGHT_KEY])
        self.slider.click()
        RESULT = float(self.result.get_text())
        range_to_move = int((MAX_SLIDER - RESULT - MIN_SLIDER) / STEP_SLIDER)
        for i in range(range_to_move):
            self.slider.send_keys(DIRECTION, False)
        return self.result.get_text()

    def return_min_and_max_slider(self):
        return (float(self.slider.get_attribute("min")), float(self.slider.get_attribute("max")))