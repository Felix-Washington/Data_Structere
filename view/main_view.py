import PySimpleGUI as sg


class MainView:
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def start_screen(self):
        layout = [[sg.Button("Stack", size=(10, 2))],
                  [sg.Button("Queue", size=(10, 2))],
                  [sg.Button("Back", size=(10, 2))]]
        self.__window = sg.Window("Choose an option", default_element_size=(100, 50)).Layout(layout)
        return self.open()
