import PySimpleGUI as sg


class StackView:
    def __init__(self):
        self.__window = None

    # Open window
    def open(self):
        button, values = self.__window.Read()
        return button, values

    # Close window
    def close(self):
        self.__window.Close()

    # Options with stack
    def options(self):
        layout = [[sg.Button("Create Stack", size=(10, 2))],
                  [sg.Button("View Stack", size=(10, 2))],
                  [sg.Button("Back", size=(10, 2))]]

        self.__window = sg.Window("Choose an option").Layout(layout)

        return self.open()

    # Create a stack
    def create(self):
        layout = [[sg.Text("Size of stack")],
                  [sg.InputText()],

                  [sg.Submit("Create"), sg.Button("Cancel")]]

        self.__window = sg.Window("Size of stack").Layout(layout)

        return self.open()

    # Show operations of the stack
    def view(self, stacks):
        layout = [[sg.Text("Stacks")],
                  [sg.Listbox(values=stacks, size=(30, 5))],

                  [sg.Button("Add"), sg.Button("Remove"), sg.Button("View")],
                  [sg.Button("Remove Stack"), sg.Button("Back")]]

        self.__window = sg.Window("").Layout(layout)

        return self.open()

    # Type a value to create a stack
    def number(self):
        layout = [[sg.Text("Type a number")],
                  [sg.InputText()],

                  [sg.Submit("Submit"), sg.Button("Cancel")]]

        self.__window = sg.Window("Fill").Layout(layout)

        return self.open()

    # Show stack data
    def show_stack(self, stack_data, stack_length, stack_top):

        layout = [
            [sg.Text("Stack values:", size=(10, 1))],
            [sg.Text(stack_data)],
            [sg.Text("Stack Length: "), sg.Text(stack_length)],

            [sg.Text("Top: "), sg.Text(stack_top)],

            [sg.Button("Back")]]

        self.__window = sg.Window("Stack Values", default_element_size=(100, 50)).Layout(layout)

        return self.open()

    # Show error messages
    def show_message(self, option):

        options = {"stack_not_selected": "Stack not selected",
                   "stack_full": "The stack is full",
                   "number_zero": "Type a number highter than zero",
                   "type_value": "Type a value",
                   "stack_empty": "The stack is empty",
                   "stack_removed": "Stack is already removed, go back to update"}

        sg.Popup(options[option])