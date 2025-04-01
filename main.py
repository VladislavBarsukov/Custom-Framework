import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from pages.auth_page import Page1
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName
from base_element.base_element import BaseElement

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

#b = Page1(a)
#a.get("https://the-internet.herokuapp.com/basic_auth")
#time.sleep(1)

USERNAME = "admin"
PASSWORD = "admin"
BASE_URL = "the-internet.herokuapp.com/basic_auth"
URL_WITH_CREDENTIALS = f"https://{USERNAME}:{PASSWORD}@{BASE_URL}"

a = Browser(BrowserFactory.get_driver(AvailableDriverName.CHROME))
b = Page1(a)
a.get(URL_WITH_CREDENTIALS)
print(b.is_success_auth().text)
time.sleep(5)