import os

from resistor import Resistor


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



def get_resistor_val_files(extension):
    """
    return the list of files with the correct extension.
    :param extension: file extension with the resistor value data
    :return: a list with all the file name
    """
    all_files = os.listdir(".")
    resistor_files = list()
    for one_file in all_files:
        if extension in one_file:
            resistor_files.append(one_file)
    return resistor_files


class ResistorSolver:
    """
    find a solution to for the non-standard resistor values
    """
    _target = 0.0
    _tolerance = 0.0
    _resistor_data = list()
    _extension = ""

    def __init__(self, target, tolerance=0.05, extension=".resistor"):
        """
        create Resistor solver object, with the target values and tolerance
        :param target: target resistor value want to get
        :param tolerance: acceptable tolerance
        """
        self._target = target
        self._tolerance = tolerance
        self._extension = extension

    def solution(self):
        """
        find all the possible combination from the resistor values data
        :return: a list with resistor 1, resistor 2 and the calculated target resistor value
        """
        file_names = get_resistor_val_files(".resistor")
        val_data = self.get_data(file_names[1])
        result = list()
        val_min = self._target * (1.0 - self._tolerance)
        val_max = self._target * (1.0 + self._tolerance)
        for val_1 in val_data:
            for val_2 in val_data:
                r1 = Resistor(val=val_1)
                r2 = Resistor(val=val_2)
                rp = r1.parallel_with(r2)
                if val_min <= rp.value() <= val_max:
                    result.append([r1.value(), r2.value(), rp.value(), self._tolerance])
        return result

    def get_data(self, file_name):
        """
        open a file and extract all resistor values and put it into a list
        :param file_name: file contain the resistor values
        :return: a list with all the resistor values
        """
        data = list()
        with open(file_name) as file:
            for line in file:
                data.append(float(line.strip()))
        return data
