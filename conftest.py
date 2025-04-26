from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement

import pytest
from browser.browser_factory import BrowserFactory, AvailableDriverName


@pytest.fixture(scope="function")
def browser():
    driver = BrowserFactory.get_driver(AvailableDriverName.CHROME, ["--start-maximized"])
    browser_instance = Browser(driver)
    yield browser_instance
    browser_instance.quit()

