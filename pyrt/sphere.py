from .shape import Shape

class Sphere(Shape):
    def __init__(self, center, radius):
        self.__center = center
        self.__radius = radius

    def hit(self, ray):
        pass