import os

from resistor_dataset import ResistorDataset


class ResistorData:
    _extension = ""
    _file_list = list()
    _name_list = list()
    _value_list = list()
    _dataset_list = list()

    def __init__(self, extension):
        self._extension = extension
        self.get_files()

    def get_files(self):
        all_files = os.listdir(".")
        self._file_list.clear()
        for one_file in all_files:
            if self._extension in one_file:
                self._file_list.append(one_file)
        return self._file_list

    def get_names(self):
        self._name_list.clear()
        for file in self._file_list:
            standard = file.replace(self._extension, "")
            self._name_list.append(standard)
        return self._name_list

    def get_values(self):
        self._value_list.clear()
        for file_name in self._file_list:
            data = list()
            with open(file_name) as file:
                for line in file:
                    data.append(float(line))
            self._value_list.append(data)
        return self._value_list

    def get_dataset(self):
        self._dataset_list.clear()
        for name, data in zip(self.get_names(), self.get_values()):
            data_set = ResistorDataset(name=name, data=data)
            self._dataset_list.append(data_set)
        return self._dataset_list
