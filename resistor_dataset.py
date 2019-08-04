class ResistorDataset:
    """
    a simple class to put the resistor data in
    """
    _name = ""
    _data = list()

    def __init__(self, name, data):
        """
        ResistorData constructor
        :param name: name of the resistor data set
        :param data: resistor values in a list
        """
        self._name = name
        self._data = data

    def name(self):
        """
        :return: name of resistor data set
        """
        return self._name

    def data(self):
        """
        :return: all possible resistor value in a list
        """
        return self._data
