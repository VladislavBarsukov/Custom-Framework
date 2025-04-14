import time
import pytest
from pages.iframe_page import IframePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_iframe(browser):
    url = "https://demoqa.com/"
    q = browser
    q.get(url)
    a = IframePage(browser)
    a.open_alerts_frame_windows()
    a.open_nested_frames()
    text1 = a.switch_and_check_parent_nested_frames_text()
    assert text1 == "Parent frame", "Error"
    text2 = a.switch_and_check_child_nested_frames_text()
    assert text2 == "Child Iframe", "Error"
    a.switch_to_default()
    a.open_frames()
    text_big_frame = a.switch_and_check_big_frames_text()
    a.switch_to_default()
    text_small_frame = a.switch_and_check_small_frames_text()
    a.switch_to_default()
    assert text_big_frame == text_small_frame, "Error"