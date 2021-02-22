from model.queue import Queue
from view.queue_view import QueueView
from model.element import Element


class QueueController:

    def __init__(self):
        self.__queue_view = QueueView()
        self.__queue_list = []
        self.__queue_number = 0

    def queue_options(self):
        screen = True
        while screen:
            button, values = self.__queue_view.start_screen()

            if button == "Create":
                self.create()

            elif button == "View":
                self.view()

            elif button == "Back":
                screen = False

            self.__queue_view.close()

    def create(self):
        screen = True
        while screen:
            button, values = self.__queue_view.create()

            if button == "Back":
                screen = False
            elif values[0] == "":
                self.__queue_view.show_message("type_value")

            elif button == "Create":
                queue_length = int(values[0])
                if queue_length <= 0:
                    self.__queue_view.show_message("number_zero")
                else:
                    self.__queue_number += 1
                    queue = Queue(queue_length, self.__queue_number)
                    self.__queue_list.append(queue)
                    screen = False

            self.__queue_view.close()

    def view(self):
        scren_opened = True
        queue_numbers_list = []
        for queue in self.__queue_list:
            number = queue.number
            queue_numbers_list.append(number)

        while scren_opened:
            button, values = self.__queue_view.view(queue_numbers_list)

            if button == "Back":
                scren_opened = False

            elif not values[0]:
                self.__queue_view.show_message("queue_not_selected")

            else:
                queue_chosen = None

                for one_queue in self.__queue_list:
                    if one_queue.number == int(values[0][0]):
                        queue_chosen = one_queue

                if button == "Add":
                    self.__queue_view.close()
                    self.add_value(queue_chosen)

                elif button == "Remove":
                    self.remove_value(queue_chosen)

                elif button == "View":
                    self.__queue_view.close()
                    self.view_queue(queue_chosen)

                elif button == "Remove Queue":
                    self.remove_queue(queue_chosen)

            self.__queue_view.close()

    def add_value(self, queue_chosen):
        screen = True
        while screen:
            button, values = self.__queue_view.add_values()

            if button == "Submit":
                if values != {0: ""}:
                    if queue_chosen.elements_number == 0:
                        element = Element(int(values[0]), None)
                        queue_chosen.values.append(element)
                        queue_chosen.first = element

                    elif queue_chosen.elements_number < queue_chosen.length:
                        element = Element(int(values[0]), None)
                        queue_chosen.values.append(element)
                        element_index = queue_chosen.values.index(element)
                        queue_chosen.values[element_index - 1].value_before = element

                    else:
                        self.__queue_view.show_message("queue_full")
                        queue_chosen.elements_number -= 1

                        queue_chosen.last = element

                    """
                    for i in queue_chosen.values:
                        print("values", i.value)
                        if i.value_before != None:
                            print("values before", i.value_before.value)
                        else:
                            print("values before", i.value_before)
                    """

                    queue_chosen.last = element
                    queue_chosen.elements_number += 1
                else:
                    self.__queue_view.show_message("type_value")
            else:
                screen = False
            self.__queue_view.close()
        self.__queue_list[queue_chosen.number - 1] = queue_chosen

    def remove_value(self, queue_chosen):
        if queue_chosen.elements_number == 1:
            queue_chosen.values.remove(queue_chosen.first)
            queue_chosen.first = None
            #queue_chosen.last = None

        elif queue_chosen.elements_number > 0:
            queue_chosen.values.remove(queue_chosen.first)
            queue_chosen.first = queue_chosen.values[0]

        else:
            self.__queue_view.show_message("queue_empty")
            queue_chosen.elements_number += 1

        queue_chosen.elements_number -= 1
        self.__queue_list[queue_chosen.number - 1] = queue_chosen

    def view_queue(self, queue_chosen):
        screen = True
        elements_value = []
        while screen:
            if queue_chosen.elements_number > 0:
                for i in range(queue_chosen.elements_number, 0, -1):
                    elements_value.append(queue_chosen.values[i - 1].value)

            if queue_chosen.first is None and queue_chosen.first is None:
                button, values = self.__queue_view.show_queue(elements_value, queue_chosen.length, None, None)


            else:
                button, values = self.__queue_view.show_queue(elements_value, queue_chosen.length,
                                                              queue_chosen.first.value, queue_chosen.last.value)

            if button == "Back":
                screen = False

            self.__queue_view.close()

    def remove_queue(self, queue_chosen):
        if queue_chosen is None:
            self.__queue_view.show_message("queue_removed")
        else:
            self.__queue_list.remove(queue_chosen)
