

class Stack:
    def __init__(self, length: int, number):
        self.__length = length  # Stack length
        self.__top = None  # Element in the top of stack
        self.__number = number  # Stack ID
        self.__stack_elements = []  # Stake elements list
        self.__elements_quantity = 0  # Quantity elements inside of the stack

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        self.__top = top

    @property
    def stack_elements(self):
        return self.__stack_elements

    @stack_elements.setter
    def stack_elements(self, stack_elements):
        self.__stack_elements = stack_elements

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def elements_quantity(self):
        return self.__elements_quantity

    @elements_quantity.setter
    def elements_quantity(self, elements_quantity):
        self.__elements_quantity = elements_quantity

    def add_number_stack(self, number):
        self.__stack_elements.append(number)