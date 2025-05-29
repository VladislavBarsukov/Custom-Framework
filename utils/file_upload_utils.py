import os
import autoit
import subprocess
import time


class UploadImageUtils:
    TIME_SLEEP_FOR_DRAG_AND_DROP = 5

    def upload_to_red_square(self, file_path):
        autoit_script_path = os.path.join(os.getcwd(), "upload_1.exe")
        subprocess.run([autoit_script_path, file_path])

    def drag_and_drop_upload(self, file_path, red_square_x, red_square_y):
        autoit_script_path = os.path.join(os.getcwd(), "upload_2.exe")
        subprocess.Popen([autoit_script_path, file_path, str(red_square_x), str(red_square_y)])
        time.sleep(self.TIME_SLEEP_FOR_DRAG_AND_DROP)
