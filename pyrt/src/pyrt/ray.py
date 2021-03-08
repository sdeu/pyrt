from dataclasses import dataclass
from .vec3 import Vec3
from .point import Point3


@dataclass
class Ray:
    origin: Point3
    direction: Vec3

    def point_at(self, t):
        return self.__origin + (t * self.__direction)

    def __str__(self):
        return f'{self.origin} + t*{self.direction}'
