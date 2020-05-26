from .vec3 import Vec3
from .point import Point3

class Ray:
    def __init__(self, orig=Point3(0,0,0), d=Vec3(1,0,0)):
        self.__origin = orig
        self.__direction = d

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    def point_at(self, t):
        return self.__origin + (t * self.__direction)

    def __str__(self):
        return f'{self.origin} + t*{self.direction}'