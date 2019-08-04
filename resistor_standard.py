class ResistorStandard:
    """
    a simple class to put the resistor data in
    """
    _standard = ""
    _list = list()

    def __init__(self, standard, data):
        """
        ResistorData constructor
        :param standard: name of the resistor standard
        :param data: resistor values in a list
        """
        self._standard = standard
        self._list = data

    def name(self):
        """
        :return: resistor standard
        """
        return self._standard

    def data(self):
        """
        :return: all possible resistor value in a list
        """
        return self._list
