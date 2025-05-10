import pytest
from pages.alert_page import AlertPage
import json


def test_alerts(browser):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["javascript_alerts_page"]
    text_for_prompt = "alert"
    browser.get(url)
    alert_js_page = AlertPage(browser)
    get_js_alert = alert_js_page.get_js_alert()
    assert get_js_alert == "You successfully clicked an alert", f"ERROR"
    get_js_confirm_ok = alert_js_page.get_js_confirm_ok()
    assert get_js_confirm_ok == "You clicked: Ok", f"ERROR"
    get_js_confirm_cancel = alert_js_page.get_js_confirm_cancel()
    assert get_js_confirm_cancel == "You clicked: Cancel", f"ERROR"
    get_js_prompt_ok = alert_js_page.get_js_prompt_ok(text_for_prompt)
    assert get_js_prompt_ok == f"You entered: {text_for_prompt}", f"ERROR"
    get_js_prompt_cancel = alert_js_page.get_js_prompt_cancel(text_for_prompt)
    assert get_js_prompt_cancel == f"You entered: null", f"ERROR"
