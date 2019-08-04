from resistor import Resistor
from resistor_data import ResistorData


class ResistorSolver:
    """
    find a solution to for the non-standard resistor values
    """
    _target = Resistor()
    _dataset_list = list()

    def __init__(self, target, tolerance=0.05, extension=".resistor"):
        """
        create Resistor solver object, with the target values and tolerance
        :param target: target resistor value
        :param tolerance: acceptable tolerance
        """
        self._target = Resistor(val=target, tolerance=tolerance)
        # extract the data from the data set file and put them into a data set list
        self._dataset_list = ResistorData(extension).get_dataset()

    def solution(self):
        """

        :return:
        """
        result = list()
        # loop through all data set
        for data_set in self._dataset_list:
            # loop through all the values
            index = 0
            for val_1 in data_set.data():
                index = index + 1
                for val_2 in data_set.data()[index:]:
                    r1 = Resistor(val=val_1)
                    r2 = Resistor(val=val_2)
                    rp = r1.parallel_with(r2)
                    if self._target.value_min() <= rp.value() <= self._target.value_max():
                        error = (self._target.value() - rp.value()) / self._target.value()
                        result.append([data_set.name(), r1.value(), r2.value(), rp.value(), error])
        return result

