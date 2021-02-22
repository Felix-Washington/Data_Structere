

class Element:
    def __init__(self, value, value_before):
        self.__value = value
        self.__value_before = value_before

    @property
    def value(self):
        return self.__value

    @property
    def value_before(self):
        return self.__value_before

    @value_before.setter
    def value_before(self, value_before):
        self.__value_before = value_before
