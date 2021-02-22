import PySimpleGUI as sg


class QueueView:
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def start_screen(self):
        layout = [[sg.Button("Create", size=(10, 2))],
                  [sg.Button("View", size=(10, 2))],
                  [sg.Button("Back", size=(10, 2))]]
        self.__window = sg.Window("Choose an option", default_element_size=(100, 50)).Layout(layout)
        return self.open()

    def create(self):
        layout = [
            [sg.Text("Size of queue")],
            [sg.InputText()],
            [sg.Button("Create", size=(10, 2))], [sg.Button("Back", size=(10, 2))]]

        self.__window = sg.Window("Choose an option", default_element_size=(10, 2)).Layout(layout)
        return self.open()

    def view(self, queues):
        layout = [[sg.Text("Queues")],
                  [sg.Listbox(values=queues, size=(30, 5))],

                  [sg.Button("Add"), sg.Button("Remove"), sg.Button("View")],
                  [sg.Button("Remove Queue"), sg.Button("Back")]]

        self.__window = sg.Window("").Layout(layout)

        return self.open()

    def show_queue(self, queue_data, queue_length, first, last):

        layout = [
            [sg.Text("Queue values:", size=(10, 1))],
            [sg.Text(queue_data)],
            [sg.Text("Queue Length:"), sg.Text(queue_length)],
            [sg.Text("First value:"), sg.Text(first)],
            [sg.Text("Last value:"), sg.Text(last)],
            [sg.Button("Back")]]

        self.__window = sg.Window("Queue Values").Layout(layout)

        return self.open()

    def add_values(self):
        layout = [[sg.Text("Type a number")],
                  [sg.InputText()],

                  [sg.Submit("Submit"), sg.Button("Cancel")]]

        self.__window = sg.Window("Fill").Layout(layout)

        return self.open()

    def show_message(self, message):
        messages = {"number_zero": "Type a number highter than zero",
                    "type_value": "Type a value",
                    "queue_full": "Queue is full",
                    "queue_not_selected": "Queue not selected",
                    "queue_empty": "The Queue is empty",
                    "queue_removed": "Queue is already removed, go back to update"}

        sg.Popup(messages[message])