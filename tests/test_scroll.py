import json
import pytest
from pages.infinity_scroll_page import ScrollPage


@pytest.mark.parametrize("count_of_text", [10])
def test_scroll(browser, count_of_text):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["scroll_page"]
    browser.get(url)
    scroll_page = ScrollPage(browser)
    text_elements = []
    while len(text_elements) < count_of_text:
        i = scroll_page.find_text_elements()
        browser.scroll_into_view(scroll_page.find_last_element())
        for j in i:
            if j not in text_elements and len(text_elements) < count_of_text:
                text_elements.append(j)
    assert len(text_elements) == count_of_text, f"Expect get {count_of_text} elements, but get {len(text_elements)}"
