import pytest
from pages.image_page import ImagePage
from pages.after_upload_image_page import AfterUploadImagePage
import os
import json


def test_image(browser):
    with open("urls.json", "r") as f:
        urls = json.load(f)
    url = urls["image_page"]
    browser.get(url)
    image_page = ImagePage(browser)
    file_name = "test_file.txt"
    temp_dir = os.path.join(os.getcwd(), "temp_upload")
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, file_name)
    with open(file_path, "w") as f:
        f.write("This is a test file.")
    image_page.upload_image(file_path)
    os.remove(file_path)
    image_page_after = AfterUploadImagePage(browser)
    image_page_after.wait_for_open()
    text = image_page_after.get_result_of_upload_text()
    file_name_text = image_page_after.get_result_of_upload_file()
    assert text == "File Uploaded!", f"ERROR, expected text = File Uploaded!, get text = {text}"
    assert file_name_text == file_name, f"ERROR, expected file_name_text = {file_name}, get file_name_text = {file_name}"
