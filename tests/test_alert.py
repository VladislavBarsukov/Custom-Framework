import pytest
from pages.alert_page import AlertPage
import json


def test_alerts(browser, urls):
    url = urls["javascript_alerts_page"]
    text_for_prompt = "alert"
    browser.get(url)
    alert_page = AlertPage(browser)
    get_alert = alert_page.get_js_alert()
    assert get_alert == "You successfully clicked an alert", f"ERROR, expected get_js_alert = You successfully clicked an alert, get {get_alert}"
    get_confirm_ok = alert_page.get_js_confirm_ok()
    assert get_confirm_ok == "You clicked: Ok", f"ERROR, expected get_js_confirm_ok = You clicked: Ok, get {get_confirm_ok}"
    get_confirm_cancel = alert_page.get_js_confirm_cancel()
    assert get_confirm_cancel == "You clicked: Cancel", f"ERROR, expected get_js_confirm_cancel = You clicked: Cancel, get {get_confirm_cancel}"
    get_prompt_ok = alert_page.get_js_prompt_ok(text_for_prompt)
    assert get_prompt_ok == f"You entered: {text_for_prompt}", f"ERROR, expected get_js_prompt_ok = You entered: {text_for_prompt}, get {get_prompt_ok}"
    get_prompt_cancel = alert_page.get_js_prompt_cancel(text_for_prompt)
    assert get_prompt_cancel == f"You entered: null", f"ERROR, expected get_js_prompt_cancel = You entered: null, get {get_prompt_cancel}"
