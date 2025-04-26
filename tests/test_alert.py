import pytest
from pages.alert_page import AlertPage


def test_alerts(browser):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    text_for_prompt = "alert"
    browser.get(url)
    alert_page = AlertPage(browser)
    get_js_alert = alert_page.get_js_alert()
    assert get_js_alert == "You successfully clicked an alert", f"ERROR, expected get_js_alert = You successfully clicked an alert, get {get_js_alert}"
    get_js_confirm_ok = alert_page.get_js_confirm_ok()
    assert get_js_confirm_ok == "You clicked: Ok", f"ERROR, expected get_js_confirm_ok = You clicked: Ok, get {get_js_confirm_ok}"
    get_js_confirm_cancel = alert_page.get_js_confirm_cancel()
    assert get_js_confirm_cancel == "You clicked: Cancel", f"ERROR, expected get_js_confirm_cancel = You clicked: Cancel, get {get_js_confirm_cancel}"
    get_js_prompt_ok = alert_page.get_js_prompt_ok(text_for_prompt)
    assert get_js_prompt_ok == f"You entered: {text_for_prompt}", f"ERROR, expected get_js_prompt_ok = You entered: {text_for_prompt}, get {get_js_prompt_ok}"
    get_js_prompt_cancel = alert_page.get_js_prompt_cancel(text_for_prompt)
    assert get_js_prompt_cancel == f"You entered: null", f"ERROR, expected get_js_prompt_cancel = You entered: null, get {get_js_prompt_cancel}"
