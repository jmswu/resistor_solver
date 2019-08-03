import os

from resistor import Resistor


def get_resistor_val_files(extension):
    all_files = os.listdir(".")
    resistor_files = list()
    for one_file in all_files:
        if extension in one_file:
            resistor_files.append(one_file)
    return resistor_files


class ResistorSolver:
    _target = 0.0
    _tolerance = 0.0

    def __init__(self, target, tolerance=0.05):
        self._target = target
        self._tolerance = tolerance

    def solution(self):
        file_names = get_resistor_val_files(".resistor")
        val_data = self.get_data(file_names[0])
        result = list()
        val_min = self._target * (1.0 - self._tolerance)
        val_max = self._target * (1.0 + self._tolerance)
        for val_1 in val_data:
            for val_2 in val_data:
                r1 = Resistor(val=val_1)
                r2 = Resistor(val=val_2)
                rp = r1.parallel_with(r2)
                if val_min <= rp.value() <= val_max:
                    result.append([r1.value(), r2.value(), rp.value()])
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
