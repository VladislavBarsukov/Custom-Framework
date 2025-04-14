import pytest
from pages.alert_js_page import AlertJsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_alerts(browser):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    text_for_prompt="alert"
    browser.get(url)
    b = AlertJsPage(browser)
    get_js_alert = b.get_js_alert()
    assert get_js_alert=="You successfully clicked an alert", f"ERROR"
    get_js_confirm_ok = b.get_js_confirm_ok()
    assert get_js_confirm_ok == "You clicked: Ok", f"ERROR"
    get_js_confirm_cancel = b.get_js_confirm_cancel()
    assert get_js_confirm_cancel == "You clicked: Cancel", f"ERROR"
    get_js_prompt_ok = b.get_js_prompt_ok(text_for_prompt)
    assert get_js_prompt_ok == f"You entered: {text_for_prompt}", f"ERROR"
    get_js_prompt_cancel = b.get_js_prompt_cancel(text_for_prompt)
    assert get_js_prompt_cancel == f"You entered: null", f"ERROR"