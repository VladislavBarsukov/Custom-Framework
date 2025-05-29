import pytest
from pages.iframe_page import IframePage
from pages.main_frame_page import MainFramePage
import json


def test_iframe(browser, urls):
    url = urls["iframe_page"]
    browser.get(url)
    main_frame_page = MainFramePage(browser)
    main_frame_page.open_alerts_frame_windows()
    iframe_page = IframePage(browser)
    iframe_page.open_nested_frames()
    text1 = iframe_page.switch_and_get_parent_nested_frames_text()
    assert text1 == "Parent frame", f"Expected text1 = Parent Iframe get text1 = {text1}"
    text2 = iframe_page.switch_and_get_child_nested_frames_text()
    assert text2 == "Child Iframe", f"Expected text2 = Child Iframe get text2 = {text2}"
    iframe_page.open_frames()
    text_big_frame = iframe_page.switch_and_get_big_frames_text()
    text_small_frame = iframe_page.switch_and_get_small_frames_text()
    assert text_big_frame == text_small_frame, f"{text_big_frame} != {text_small_frame}"
