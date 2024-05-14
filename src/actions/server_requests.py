import requests
from PySide6 import QtWidgets

from src.ui.ui_image_adding import Ui_sendImageDialog


class ServerConnection:
    def __init__(self):
        self.server_url = "http://localhost:8080/"

    def get_list(self, addition: str, option: str):
        r = requests.get(self.server_url + addition)
        r = r.json()
        if addition == "get-properties" or addition == "get-races" or addition == "get-all-images":
            data = dict(r)
            return list(map(str, data.get(option)))
        data = list(map(dict, r))
        return [str(d.get(option)) for d in data]

    def get_list_by(self, option: str, value: str):
        r = requests.get(self.server_url + "get-images-by/" + option + "/" + value).json()
        data = dict(r)
        return list(map(str, data.get("uris")))

    def set_options_lists_for_image_adding(self, window: Ui_sendImageDialog):
        properties = self.get_list("get-properties", "properties")
        names = self.get_list("get-persons", "name")
        races = self.get_list("get-races", "races")
        genders = ["male", "female"]

        window.optionsComboBox.clear()
        window.nameComboBox.clear()
        window.raceComboBox.clear()
        window.genderComboBox.clear()

        for prop in properties:
            window.optionsComboBox.addItem(prop)
        for name in names:
            window.nameComboBox.addItem(name)
        for race in races:
            window.raceComboBox.addItem(race)
        for gender in genders:
            window.genderComboBox.addItem(gender)

    def send_image(self, file_name: str, name: str, properties: list):
        file = {"file": open(file_name, "rb")}
        data = {'personName': name, 'properties': properties}
        r = requests.post(self.server_url + "upload", files=file, data=data)
        print(r.json())

    def download_image(self, url: str):
        r = requests.get(url)
        return r.content

    def get_images(self, option: str = None, value: str = None):
        if option is None:
            res = requests.get(self.server_url + "get-all-images-info").json()
        else:
            res = requests.get(self.server_url + "get-images/" + option + "/" + value).json()

        return list(map(dict, res))

    def get_images_for_testing_by_option(self, option: str):
        res = requests.get(self.server_url + "get-images-info-by-testing-option/" + option).json()
        return list(map(dict, res))

    def get_count_of_images_by_property(self, prop: str) -> int:
        res = requests.get(self.server_url + "get-count-of-images-by-property/" + prop).json()
        return dict(res)["value"]

