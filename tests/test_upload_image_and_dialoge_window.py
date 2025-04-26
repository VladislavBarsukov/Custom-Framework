import pytest
from pages.image_page import ImagePage
from pages.after_upload_image_page import AfterUploadImagePage
import os


def test_image(browser):
    url = "https://the-internet.herokuapp.com/upload"
    browser.get(url)
    image_page = ImagePage(browser)
    file_name = "test_file.txt"
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, "w") as f:
        f.write("This is a test file.")
    image_page.click_and_upload_red_square(file_path)
    text = image_page.get_text_uploaded_file()
    success_element = image_page.get_success_mark()
    assert text == file_name, f"ERROR, expected text = {file_name}, get text = {text}"
    assert success_element == "✔", "ERROR"
