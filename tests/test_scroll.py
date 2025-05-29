import json
import pytest
from pages.infinity_scroll_page import ScrollPage


@pytest.mark.parametrize("count_of_text", [5])
def test_scroll(browser, urls, count_of_text):
    url = urls["scroll_page"]
    browser.get(url)
    scroll_page = ScrollPage(browser)
    text_elements = []
    while len(text_elements) < count_of_text:
        i = scroll_page.find_text_elements()
        for j in i:
            if j not in text_elements and len(text_elements) < count_of_text:
                text_elements.append(j)
        scroll_page.scroll_to_last_element()
    assert len(text_elements) == count_of_text, f"Expected {count_of_text} elements, but get {len(text_elements)}"
