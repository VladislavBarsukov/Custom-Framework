from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from elements.base_element import BaseElement
from config import Config
import pytest
from browser.browser_factory import BrowserFactory, AvailableDriverName
import json

@pytest.fixture(scope="function")
def browser():
    driver = BrowserFactory.get_driver(AvailableDriverName.CHROME, [Config.BROWSER_MAX_WINDOW])
    browser_instance = Browser(driver)
    yield browser_instance
    browser_instance.quit()

@pytest.fixture(scope="function")
def urls():
    with open("urls.json", "r") as f:
        return json.load(f)