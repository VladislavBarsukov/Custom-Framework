import pytest
import json
from pages.image_page import ImagePage
from pages.after_upload_image_page import AfterUploadImagePage
from utils.file_upload_utils import UploadImageUtils
import os


def test_drag_and_drop(browser, urls):
    url = urls["image_page"]
    browser.get(url)
    image_page = ImagePage(browser)
    file_name = "test_file.txt"
    temp_dir = os.path.join(os.getcwd(), "temp_upload")
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, file_name)
    with open(file_path, "w") as f:
        f.write("This is a test file.")
    file_upload = UploadImageUtils()
    location = image_page.drag_and_drop_location()
    file_upload.drag_and_drop_upload(file_path, location[0], location[1])
    text = image_page.get_text_uploaded_file()
    success_element = image_page.get_success_mark()
    assert text == file_name, f"Expected text = {file_name}, get text = {text}"
    assert success_element == "✔", f"Expected ✔, get {success_element}"
