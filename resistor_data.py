import os

from resistor_dataset import ResistorDataset


class ResistorData:
    """
    Extract all info from .resistor file into data set
    """
    _extension = ""
    _file_list = list()  # list of all files
    _name_list = list()  # list of all .resistor file
    _value_list = list()  # list of all values in .resistor file
    _dataset_list = list()  # list of names and values of .resistor file

    def __init__(self, extension):
        """
        Constructor
        :param extension: extension of files that contain all data, usually .resistor
        """
        self._extension = extension
        self.get_files()

    def get_files(self):
        """
        get a list of files with the correct extension
        :return: list of resistor files
        """
        all_files = os.listdir(".")
        self._file_list.clear()
        for one_file in all_files:
            if self._extension in one_file:
                self._file_list.append(one_file)
        return self._file_list

    def get_names(self):
        """
        get the name (excluding extension) of all resistor file
        :return: name of all resistor file
        """
        self._name_list.clear()
        for file in self._file_list:
            standard = file.replace(self._extension, "")
            self._name_list.append(standard)
        return self._name_list

    def get_values(self):
        """
        get a list of all data in all the resistor file
        :return: a list of all data in resistor file
        """
        self._value_list.clear()
        # loop through all files
        for file_name in self._file_list:
            # get the base data set from the file
            base_data = list()
            with open(file_name) as file:
                for line in file:
                    base_data.append(float(line))
            # generate full data set from base data set
            full_data = list()
            for val in [1, 10, 100, 1000, 10000, 100000, 1000000]:
                generated_data = [x * val for x in base_data]
                full_data.extend(generated_data)
            self._value_list.append(full_data)
        return self._value_list

    def get_dataset(self):
        """
        Construct data set from name list and value list
        :return: data set
        """
        self._dataset_list.clear()
        for name, data in zip(self.get_names(), self.get_values()):
            data_set = ResistorDataset(name=name, data=data)
            self._dataset_list.append(data_set)
        return self._dataset_list
