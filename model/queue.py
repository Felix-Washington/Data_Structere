

class Queue:
    def __init__(self, length, number):
        self.__first = None  # Queue's first element
        self.__last = None  # Queue's first element
        self.__length = length  # Queue's length
        self.__values = []  # List of queue's elements
        self.__number = number  # Queue ID
        self.__elements_number = 0  # Quantity elements inside of the queue

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, first):
        self.__first = first

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, last):
        self.__last = last

    @property
    def elements_number(self):
        return self.__elements_number

    @elements_number.setter
    def elements_number(self, elements_number):
        self.__elements_number = elements_number

    def add_number_queue(self, number):
        self.__values.append(number)