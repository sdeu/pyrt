from dataclasses import dataclass

from point import Point3
from vec3 import Vec3


@dataclass
class Ray:
    origin: Point3
    direction: Vec3

    def point_at(self, t):
        return self.origin + (t * self.direction)

    def __str__(self):
        return f'{self.origin} + t*{self.direction}'
