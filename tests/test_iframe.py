import pytest
from pages.iframe_page import IframePage


def test_iframe(browser):
    url = "https://demoqa.com/"
    browser.get(url)
    iframe_page = IframePage(browser)
    iframe_page.open_alerts_frame_windows()
    iframe_page.open_nested_frames()
    text1 = iframe_page.switch_and_check_parent_nested_frames_text()
    assert text1 == "Parent frame", f"Error, expected text1 = Parent Iframe get text1 = {text1}"
    text2 = iframe_page.switch_and_check_child_nested_frames_text()
    assert text2 == "Child Iframe", f"Error, expected text2 = Child Iframe get text2 = {text2}"
    iframe_page.switch_to_default()
    iframe_page.open_frames()
    text_big_frame = iframe_page.switch_and_check_big_frames_text()
    iframe_page.switch_to_default()
    text_small_frame = iframe_page.switch_and_check_small_frames_text()
    iframe_page.switch_to_default()
    assert text_big_frame == text_small_frame, f"Error {text_big_frame} != {text_small_frame}"
