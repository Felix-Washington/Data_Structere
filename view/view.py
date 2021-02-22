from abc import ABC
from abc import abstractmethod



class View(ABC):
    def __init__(self):
        self.__window = None

    @abstractmethod
    def show_message(self):
        pass