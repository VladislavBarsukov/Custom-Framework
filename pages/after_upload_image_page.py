from .base_page import BasePage
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement
from base_element.web_element import WebElement


class AfterUploadImagePage(BasePage):
    UPLOAD_RESULT = '//*[contains(text(),"File Uploaded!")]'
    UPLOAD_FILE = 'uploaded-files'

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.upload_result = WebElement(self.browser, self.UPLOAD_RESULT,
                                        description="AfterUploadImagePage -> upload_result")
        self.upload_file = WebElement(self.browser, self.UPLOAD_FILE,
                                      description="AfterUploadImagePage -> upload_file")

    def get_result_of_upload_text(self):
        return self.upload_result.get_text()

    def get_result_of_upload_file(self):
        return self.upload_file.get_text()
