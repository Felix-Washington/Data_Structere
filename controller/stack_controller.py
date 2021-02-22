from view.stack_view import StackView
from model.stack import Stack
from model.element import Element


class StackController:
    def __init__(self):
        self.__stack_view = StackView()
        self.__stacks = []
        self.__stack_number = 0

    def stack_options(self):
        screen = True

        while screen:
            button, values = self.__stack_view.options()

            if button == "Create Stack":
                self.__stack_view.close()
                self.create_stack()
            elif button == "View Stack":
                self.view_stack()
            elif button == "Back":
                screen = False

            self.__stack_view.close()

    def create_stack(self):
        screen = True

        while screen:
            button, values = self.__stack_view.create()
            if button == "Cancel":
                screen = False
            elif values[0] == "":
                self.__stack_view.show_message("type_value")

            elif button == "Create":
                stack_length = int(values[0])
                if stack_length <= 0:
                    self.__stack_view.show_message("number_zero")
                else:
                    self.__stack_number += 1
                    stack = Stack(stack_length, self.__stack_number)
                    self.__stacks.append(stack)
                    screen = False
            self.__stack_view.close()

    def remove_stack(self, stack_chosen):
        if stack_chosen is None:
            self.__stack_view.show_message("stack_removed")
        else:
            self.__stacks.remove(stack_chosen)

    def view_stack(self):
        screen_opened = True
        stack_numbers_list = []
        for stack in self.__stacks:
            number = stack.number
            stack_numbers_list.append(number)

        while screen_opened:

            button, values = self.__stack_view.view(stack_numbers_list)
            stack_chosen = None

            if button == "Back":
                screen_opened = False

            elif not values[0]:
                self.__stack_view.show_message("stack_not_selected")

            else:
                for one_stack in self.__stacks:
                    if one_stack.number == int(values[0][0]):
                        stack_chosen = one_stack

                self.__stack_view.close()
                if button == "Add":

                    self.add_value(stack_chosen)

                elif button == "Remove":
                    self.remove_value(stack_chosen)

                elif button == "View":
                    #self.__stack_view.close()
                    self.view(stack_chosen)

                elif button == "Remove Stack":
                    self.remove_stack(stack_chosen)

            self.__stack_view.close()

    def add_value(self, stack_chosen):
        screen = True

        while screen:
            button, values = self.__stack_view.number()
            if button == "Submit":

                if values != {0: ""}:
                    element_value = int(values[0])
                    if stack_chosen.elements_quantity == 0:
                        element = Element(element_value, None)
                        stack_chosen.stack_elements.append(element)
                        stack_chosen.top = element

                    elif stack_chosen.elements_quantity < stack_chosen.length:
                        element = Element(element_value, stack_chosen.top)
                        stack_chosen.stack_elements.append(element)
                        stack_chosen.top = element
                    else:
                        self.__stack_view.show_message("stack_full")
                        stack_chosen.elements_quantity -= 1

                    stack_chosen.elements_quantity += 1

                else:
                    self.__stack_view.show_message("type_value")
            else:
                screen = False

            self.__stack_view.close()
        self.__stacks[stack_chosen.number - 1] = stack_chosen

    def remove_value(self, stack_chosen):
        if stack_chosen.elements_quantity > 0:
            stack_chosen.stack_elements.remove(stack_chosen.top)
            stack_chosen.top = stack_chosen.top.value_before
            stack_chosen.elements_quantity -= 1

            self.__stacks[stack_chosen.number - 1] = stack_chosen
        else:
            self.__stack_view.show_message("stack_empty")

    def view(self, stack_chosen):
        screen = True
        while screen:
            elements_value = []

            if stack_chosen.elements_quantity > 0:
                for i in range(stack_chosen.elements_quantity, 0, -1):
                    elements_value.append(stack_chosen.stack_elements[i - 1].value)

            if stack_chosen.top is None:
                button, values = self.__stack_view.show_stack(elements_value, stack_chosen.length, None)
            else:
                button, values = self.__stack_view.show_stack(elements_value, stack_chosen.length,
                                                              stack_chosen.top.value)

            if button == "Back":
                screen = False

            self.__stack_view.close()
