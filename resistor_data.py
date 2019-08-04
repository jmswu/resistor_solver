import os


class ResistorData:
    _extension = ""
    _resistor_files = list()
    _resistor_standard_names = list()
    _resistor_data = list()
    _dict = dict()

    def __init__(self, extension=".resistor"):
        self._extension = extension
        self.get_files()

    def get_files(self):
        all_files = os.listdir(".")
        self._resistor_files.clear()
        for one_file in all_files:
            if self._extension in one_file:
                self._resistor_files.append(one_file)
        return self._resistor_files

    def get_names(self):
        self._resistor_standard_names.clear()
        for file in self._resistor_files:
            standard = file.replace(self._extension, "")
            self._resistor_standard_names.append(standard)
        return self._resistor_standard_names

    def get_data(self):
        self._resistor_data.clear()
        for file_name in self._resistor_files:
            data = list()
            with open(file_name) as file:
                for line in file:
                    data.append(float(line))
            self._resistor_data.append(data)
        return self._resistor_data

    def get_dict(self):
        self._dict.clear()
        for key, data in zip(self.get_names(), self.get_data()):
            self._dict.update({key: data})
        return self._dict
