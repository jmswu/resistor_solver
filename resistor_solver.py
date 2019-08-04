from resistor import Resistor
from resistor_data import ResistorData


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
        file_names = ResistorData(".resistor").get_files()
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
