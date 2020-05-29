from abc import ABC, abstractmethod

class Material(ABC):

    @abstractmethod
    def color(self):
        pass


class SimpleMaterial(Material):
    
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color