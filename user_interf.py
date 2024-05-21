import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot
import json
import yaml
import xml.etree.ElementTree as ET

class TaskRunner(QRunnable):
    def __init__(self, task, *args, **kwargs):
        super().__init__()
        self.task = task
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.task(*self.args, **self.kwargs)


class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Interface Program")
        self.layout = QVBoxLayout()
        self.data_label = QLabel("Loaded data:")
        self.layout.addWidget(self.data_label)
        self.load_button = QPushButton("Load data")
        self.load_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_button)
        self.save_button = QPushButton("Save data")
        self.save_button.clicked.connect(self.save_data)
        self.layout.addWidget(self.save_button)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select file", "", "JSON Files (*.json);;YAML Files (*.yml *.yaml);;XML Files (*.xml)")
        if file_path:
            worker = TaskRunner(self.read_data, file_path)
            QThreadPool.globalInstance().start(worker)

    def read_data(self, file_path):
        if file_path.endswith(".json"):
            data = self.load_json_data(file_path)
        elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
            data = self.load_yaml_data(file_path)
        elif file_path.endswith(".xml"):
            data = self.load_xml_data(file_path)
        else:
            print("Unsupported file format.")
            return

        self.display_data(data)

    def load_json_data(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data

    def load_yaml_data(self, file_path):
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            return data

    def load_xml_data(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root

    def display_data(self, data):
        self.data_label.setText(f"Loaded data:\n{data}")

    def save_data(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save as", "", "JSON Files (*.json);;YAML Files (*.yml);;XML Files (*.xml)")
        if file_path:
            worker = TaskRunner(self.write_data, file_path)
            QThreadPool.globalInstance().start(worker)

    def write_data(self, file_path):
        data = self.data_label.text().split("\n")[-1]

        if file_path.endswith(".json"):
            self.save_json_data(data, file_path)
        elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
            self.save_yaml_data(data, file_path)
        elif file_path.endswith(".xml"):
            self.save_xml_data(data, file_path)
        else:
            print("Unsupported file format.")

    def save_json_data(self, data, file_path):
        data_dict = {"Loaded data": data}
        with open(file_path, "w") as file:
            json.dump(data_dict, file)

    def save_yaml_data(self, data, file_path):
        data_dict = {"Loaded data": data}
        with open(file_path, "w") as file:
            yaml.dump(data_dict, file)

    def save_xml_data(self, data, file_path):
        root = ET.Element("root")
        element = ET.SubElement(root, "LoadedData")
        element.text = data
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface()
    window.show()
    sys.exit(app.exec_())
