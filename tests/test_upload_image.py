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
    with open(file_name, "w") as f:
        f.write("This is a test file.")
    image_page.upload_image(file_path)
    os.remove(file_path)
    image_page_after = AfterUploadImagePage(browser)
    text = image_page_after.get_result_of_upload_text()
    file_name_text = image_page_after.get_result_of_upload_file()
    assert text == "File Uploaded!", f"ERROR, expected text = File Uploaded!, get text = {text}"
    assert file_name_text == file_name, f"ERROR, expected file_name_text = {file_name}, get file_name_text = {file_name}"
