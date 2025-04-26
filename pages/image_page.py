import time
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.button import Button
from base_element.input import Input
from base_element.web_element import WebElement
import os
import autoit
import subprocess


class ImagePage(BasePage):
    UPLOAD_ELEMENT = 'file-upload'
    UPLOAD_BUTTON = 'file-submit'
    RED_SQUARE_HIDDEN_BUTTON = "//*[@class='dz-hidden-input']"
    RED_SQUARE_BUTTON_TO_UPLOAD = 'drag-drop-upload'
    FILE_AFTER_UPLOAD = "//*[@class='dz-filename']"
    SUCCESS_ELEMENT = "//*[@class='dz-success-mark']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.upload_element = Input(self.browser, self.UPLOAD_ELEMENT,
                                    description="ImagePage -> upload_element")
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON,
                                    description="ImagePage -> upload_button")
        self.red_square_button = Button(self.browser, self.RED_SQUARE_HIDDEN_BUTTON,
                                        description="ImagePage -> red_square_button")
        self.red_square_button_click = Button(self.browser, self.RED_SQUARE_BUTTON_TO_UPLOAD,
                                              description="ImagePage -> red_square_button_click")

    def upload_image(self, file_path):
        self.upload_element.send_keys(file_path)
        self.upload_button.click()

    def click_and_upload_red_square(self, file_path):
        autoit_script_path = os.path.join(os.getcwd(), "upload_1.exe")
        self.red_square_button_click.click()
        subprocess.run([autoit_script_path, file_path])

    def drag_and_drop(self, file_path):
        autoit_script_path = os.path.join(os.getcwd(), "upload_2.exe")
        location = self.red_square_button_click.get_location()
        print(location['x'], location['y'])
        target_x = location['x'] + 200
        target_y = location['y'] + 300
        subprocess.Popen([autoit_script_path, file_path, str(target_x), str(target_y)])

    def upload_red_square(self, file_path):
        self.red_square_button.upload_file(file_path)

    def get_text_uploaded_file(self):
        self.file_after_upload = WebElement(self.browser, self.FILE_AFTER_UPLOAD,
                                            description="ImagePage -> file_after_upload")
        self.file_after_upload.wait_for_visible()
        return self.file_after_upload.get_text()

    def get_success_mark(self):
        self.success_element = WebElement(self.browser, self.SUCCESS_ELEMENT,
                                          description="ContextPage -> figure button")
        return self.success_element.get_text()
