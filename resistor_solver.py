from resistor import Resistor
from resistor_data import ResistorData


class ResistorSolver:
    """
    find a solution to for the non-standard resistor values
    """
    _target = Resistor()
    _tolerance = 0.0
    _extension = ""
    _dataset_list = list()

    def __init__(self, target, tolerance=0.05, extension=".resistor"):
        """
        create Resistor solver object, with the target values and tolerance
        :param target: target resistor value want to get
        :param tolerance: acceptable tolerance
        """
        self._target = Resistor(val=target, tolerance=tolerance)
        self._tolerance = tolerance
        self._extension = extension
        # extract the data from the data set file and put them into a data set list
        self._dataset_list = ResistorData(extension).get_dataset()

    def solution(self):
        result = list()
        for data_set in self._dataset_list:
            for val_1 in data_set.data():
                for val_2 in data_set.data():
                    r1 = Resistor(val=val_1)
                    r2 = Resistor(val=val_2)
                    rp = r1.parallel_with(r2)
                    if self._target.value_min() <= rp.value() <= self._target.value_max():
                        error = (self._target.value() - rp.value()) / self._target.value()
                        result.append([data_set.name(), r1.value(), r2.value(), rp.value(), error])
        return result

