from controller.stack_controller import StackController
from controller.queue_controller import QueueController
from view.main_view import MainView


class MainController:
    def __init__(self):
        self.__stack_controller = StackController()
        self.__queue_controller = QueueController()
        self.__main_view = MainView()

    def start(self):
        screen_opened = True
        while screen_opened:
            button, values = self.__main_view.start_screen()
            if button == "Stack":
                self.__main_view.close()
                self.__stack_controller.stack_options()

            elif button == "Queue":
                self.__main_view.close()
                self.__queue_controller.queue_options()

            else:
                screen_opened = False

            self.__main_view.close()