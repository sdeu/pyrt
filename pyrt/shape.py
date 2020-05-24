from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def hit(self, ray):
        pass