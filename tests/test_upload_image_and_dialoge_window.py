import time
import pytest
from pages.image_page import ImagePage
from pages.after_upload_image_page import AfterUploadImagePage
import os
import json
from utils.file_upload_utils import UploadImageUtils


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
    image_page.click_and_upload_red_square()
    file_upload = UploadImageUtils()
    file_upload.upload_to_red_square(file_path)
    time.sleep(2)  # ПРОБЛЕМА ИЗ_ЗА ОЖИДАНИЯ IS_EXIST 0
    text = image_page.get_text_uploaded_file()
    success_element = image_page.get_success_mark()
    assert text == file_name, f"ERROR, expected text = {file_name}, get text = {text}"
    assert success_element == "✔", "ERROR"
