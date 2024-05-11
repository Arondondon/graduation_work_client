import time

from src.actions.server_requests import ServerConnection
from src.ui.ui_testing_progress import Ui_testingProgressDialog

import os
import subprocess


class Testing:

    def __init__(self, ui: Ui_testingProgressDialog):
        self.conn = ServerConnection()
        self.images_dir = os.getcwd() + "/images"
        if not os.path.exists(self.images_dir):
            os.mkdir(self.images_dir)
        self.images_dir += "/"
        self.ui = ui
        properties_list = self.conn.get_list("get-properties", "properties")
        self.properties = dict(zip(list(map(lambda x: x.lower(), properties_list)), properties_list))
        self.sections_in_total = 0
        self.current_section_number = 0
        self.tests_passed_in_total = 0
        self.last_progress = 0
        self.cmd = ""
        self.failed_tests = []
        self.failed_tests_in_sections_count = []


    def start(self, cmd: str):
        self.failed_tests.clear()
        self.failed_tests_in_sections_count = [0] * self.sections_in_total
        self.cmd = cmd
        self.sections_in_total = 1
        self.current_section_number = 1
        self.tests_passed_in_total = 0
        self.last_progress = 0

        self.update_progress(self.sections_in_total, self.current_section_number, 0,
                             self.tests_passed_in_total, self.last_progress)

        self.simple_testing()

        print(self.tests_passed_in_total, self.failed_tests_in_sections_count, sep="\n")

    def simple_testing(self):
        images = self.conn.get_images()
        bad_properties = [self.properties["face_turned_away"], self.properties["photo"],
                          self.properties["poor_quality"], self.properties["partly_covered_face"],
                          self.properties["adversarial_attack"]]

        i = 0
        while i < len(images):
            if images[i]["properties"] in bad_properties:
                images.pop(i)
            else:
                i += 1

        tests_in_total = (len(images) * len(images)) // 2
        tests_left_in_section = tests_in_total
        local_progress = self.calculate_local_progress(tests_left_in_section, tests_in_total)

        self.update_progress(self.sections_in_total, self.current_section_number, tests_left_in_section,
                             self.tests_passed_in_total, self.last_progress + local_progress)

        for i in range(len(images) - 1):
            for j in range(i + 1, len(images)):
                expected_result = images[i]["person"] == images[j]["person"]
                actual_result = self.compare_two_images(images[i]["uri"], images[j]["uri"])

                if expected_result != actual_result:
                    self.failed_tests.append([i, j])
                    self.failed_tests_in_sections_count[self.current_section_number - 1] += 1

                tests_left_in_section -= 1
                self.tests_passed_in_total += 1
                local_progress = self.calculate_local_progress(tests_left_in_section, tests_in_total)
                self.update_progress(self.sections_in_total, self.current_section_number, tests_left_in_section,
                                     self.tests_passed_in_total, self.last_progress + local_progress)

                print(images[i]["uri"], images[j]["uri"], expected_result, actual_result)
                time.sleep(1)

    def calculate_local_progress(self, tests_left_in_section: int, tests_in_section: int):
        return ((tests_in_section - tests_left_in_section) * 100) // tests_in_section // self.sections_in_total

    def update_last_progress(self):
        self.last_progress = (self.current_section_number - 1) * 100 // self.sections_in_total

    def update_progress(self, sections_in_total: int, current_section_number: int,
                        tests_left_in_section: int, tests_passed_in_total: int, progress: int):
        self.ui.firstStatValue.setText(str(sections_in_total))
        self.ui.secondStatValue.setText(str(current_section_number))
        self.ui.thirdStatValue.setText(str(tests_left_in_section))
        self.ui.fourthStatValue.setText(str(tests_passed_in_total))
        self.ui.progressBar.setValue(progress)

    def compare_two_images(self, first_uri: str, second_uri: str):
        image_bytes_1 = self.conn.download_image(first_uri)
        image_bytes_2 = self.conn.download_image(second_uri)

        file_path_1 = self.images_dir + "first.jpg"
        with open(file_path_1, "wb") as f:
            f.write(image_bytes_1)

        file_path_2 = self.images_dir + "second.jpg"
        with open(file_path_2, "wb") as f:
            f.write(image_bytes_2)

        command = self.cmd + " " + file_path_1 + " " + file_path_2
        res = int(subprocess.check_output(command).decode('cp866'))

        os.remove(file_path_1)
        os.remove(file_path_2)

        if res == 1:
            return True
        else:
            return False


