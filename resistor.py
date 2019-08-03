class Resistor:
    """
    Resistor object
    """
    _name = ""  # name of the resistor
    _val = 0.0  # value of the resistor

    def __init__(self, val, name="Resistor"):
        """
        Create a resistor object
        :param val:     value of resistor
        :param name:    name of resistor
        """
        self._name = name
        self._val = val

    def parallel_with(self, resistor):
        """
        calculate the value of this resistor parallel with another resistor
        Their names will be combined.
        :param resistor: a resistor object
        :return: new resistor object in parallel
        """
        result = self.reciprocal() + resistor.reciprocal()
        paralleled_val = 1 / result
        paralleled_resistor = Resistor(val=paralleled_val, name=self.name() + "//" + resistor.name())
        return paralleled_resistor

    def series_with(self, resistor):
        """
        calculate the value of this resistor in series with another resistor
        Theri names will be combined
        :param resistor: a resistor object
        :return: new resistor object in series
        """
        return self.value() + resistor.value()

    def reciprocal(self):
        """
        get reciprocal value of self
        :return: reciprocal value
        """
        return 1 / self._val

    def value(self):
        """
        return resistor value
        :return: resistor value
        """
        return self._val

    def name(self):
        """
        return resistor name
        :return: resistor name
        """
        return self._name
