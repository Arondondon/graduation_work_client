# D:/PROGRAMMING/py_face_rec/venv/Scripts/python.exe D:/PROGRAMMING/py_face_rec/compare.py

from src.actions.server_requests import ServerConnection
from src.ui.ui_results import Ui_resultsDialog
from src.ui.ui_testing_progress import Ui_testingProgressDialog

from PySide6.QtGui import QPixmap

import os
import subprocess


class Testing:

    def __init__(self, ui_progress: Ui_testingProgressDialog, ui_results: Ui_resultsDialog):
        self.ui_progress = ui_progress
        self.ui_results = ui_results

        self.conn = ServerConnection()
        self.images_dir = os.getcwd() + "/images"
        if not os.path.exists(self.images_dir):
            os.mkdir(self.images_dir)
        self.images_dir += "/"

        self.TESTING_OPTIONS = ["Simple Testing",
                                "Testing with tag GRIMACE",
                                "Testing with tag HEADDRESS",
                                "Testing with tag FACE_TURNED_AWAY",
                                "Testing with tag PHOTO",
                                "Testing with tag BAD_LIGHT",
                                "Testing with tag POOR_QUALITY",
                                "Testing with tag PARTLY_COVERED_FACE",
                                "Testing with tag ADVERSARIAL_ATTACK"]
        properties = self.conn.get_list("get-properties", "properties")
        self.properties_by_testing = dict(zip(self.TESTING_OPTIONS, [
            [
                properties[2], properties[4], properties[5], properties[6],
                properties[7], properties[8], properties[9], properties[10]
            ],
            properties[2],
            properties[4],
            properties[5],
            properties[6],
            properties[7],
            properties[8],
            properties[9],
            properties[10]
        ]))

        self.sections_in_total = 0
        self.current_section_number = 0
        self.tests_passed_in_total = 0
        self.last_progress = 0
        self.cmd = ""
        self.failed_tests = []
        self.failed_tests_in_sections_count = []
        self.texts_for_results = []
        self.current_testing_options = []

    def get_testing_options(self) -> [str]:
        return self.TESTING_OPTIONS

    def start(self, cmd: str, testing_options: [str]):
        self.current_testing_options = testing_options
        self.failed_tests.clear()
        self.cmd = cmd
        self.sections_in_total = len(testing_options)
        self.failed_tests_in_sections_count = [0] * self.sections_in_total
        self.tests_passed_in_total = 0
        self.update_progress(self.sections_in_total, 1, 0, 0, 0)

        for i in range(self.sections_in_total):
            self.current_section_number = i + 1
            self.last_progress = (self.current_section_number - 1) * 100 // self.sections_in_total

            self.test_by_option(self.current_testing_options[i])

        #print(self.tests_passed_in_total, self.failed_tests_in_sections_count, sep="\n")

    def test_by_option(self, option: str):
        test_prop = self.properties_by_testing[option]

        if option == "Simple Testing":
            images = self.conn.get_images()
            i = 0
            while i < len(images):
                last_size = len(images)
                for prop in images[i]["properties"]:
                    if prop in test_prop:
                        images.pop(i)
                        break
                if last_size == len(images):
                    i += 1
            tests_in_total = (len(images) * (len(images) - 1)) // 2
        else:
            images = self.conn.get_images_for_testing_by_option(test_prop)
            num = len(images) - self.conn.get_count_of_images_by_property(test_prop)
            tests_in_total = ((len(images) * (len(images) - 1)) // 2) - ((num * (num - 1)) // 2)

        tests_left_in_section = tests_in_total
        local_progress = self.calculate_local_progress(tests_left_in_section, tests_in_total)

        self.update_progress(self.sections_in_total, self.current_section_number, tests_left_in_section,
                             self.tests_passed_in_total, self.last_progress + local_progress)

        st = (option == "Simple Testing")
        for i in range(len(images) - 1):
            fi = (test_prop in images[i]["properties"])  # first image

            for j in range(i + 1, len(images)):
                si = (test_prop in images[j]["properties"])  # second image

                if (not st) and (not fi) and (not si):
                    continue

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

                print(i, j, expected_result, actual_result)

        text = "Simple testing is a testing method that uses images in which the person's face is clearly legible \n\n"
        text += "Simple testing results:\n\n"
        text += "Total number of tests: " + str(tests_in_total) + "\n"
        text += "Tests passed: " + str(tests_in_total - self.failed_tests_in_sections_count[self.current_section_number - 1]) + "\n"
        text += "Tests failed: " + str(self.failed_tests_in_sections_count[self.current_section_number - 1]) + "\n"
        self.texts_for_results.append(text)

    def set_results(self):
        self.ui_results.firstStatValue.setText(str(self.sections_in_total))
        self.ui_results.secondStatValue.setText(str(self.tests_passed_in_total))
        self.ui_results.thirdStatValue.setText(str(sum(self.failed_tests_in_sections_count)))
        self.ui_results.sectionsComboBox.clear()
        self.ui_results.sectionsComboBox.addItems(self.current_testing_options)
        self.ui_results.resultsTextEdit.setText(self.texts_for_results[0])
        self.ui_results.firstImage.setPixmap(QPixmap(self.images_dir + "test_image_1.jpg"))
        self.ui_results.secondImage.setPixmap(QPixmap(self.images_dir + "test_image_2.jpg"))

        self.ui_results.sectionsComboBox.changeEvent()

    def calculate_local_progress(self, tests_left_in_section: int, tests_in_section: int):
        return ((tests_in_section - tests_left_in_section) * 100) // tests_in_section // self.sections_in_total

    def update_last_progress(self):
        self.last_progress = (self.current_section_number - 1) * 100 // self.sections_in_total

    def update_progress(self, sections_in_total: int, current_section_number: int,
                        tests_left_in_section: int, tests_passed_in_total: int, progress: int):
        self.ui_progress.firstStatValue.setText(str(sections_in_total))
        self.ui_progress.secondStatValue.setText(str(current_section_number))
        self.ui_progress.thirdStatValue.setText(str(tests_left_in_section))
        self.ui_progress.fourthStatValue.setText(str(tests_passed_in_total))
        self.ui_progress.progressBar.setValue(progress)

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


