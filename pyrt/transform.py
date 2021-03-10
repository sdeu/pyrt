from typing import Any
import numpy as np
from .vec3 import Vec3
from .point import Point3
from .ray import Ray


class Transform:
    def __init__(self, matrix: Any, inverse: Any = None) -> None:
        self.matrix = matrix
        self._inverse = inverse

    @property
    def inverse(self):
        if self._inverse is not None:
            return Transform(self._inverse, self.matrix)

        inv = np.linalg.inv(self.matrix)
        return Transform(inv, self.matrix)

    def __matmul__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.matrix @ other.vec)

        if isinstance(other, Point3):
            return Point3.from_array(self.matrix @ other.vec)

        if isinstance(other, Ray):
            return Ray(Point3.from_array(self.matrix @ other.origin.vec),
                       Vec3.from_array(self.matrix @ other.direction.vec))

    @classmethod
    def translation(cls, dx, dy, dz):
        matrix = np.identity(4)
        matrix[0][3] = dx
        matrix[1][3] = dy
        matrix[2][3] = dz

        inverse = np.identity(4)
        inverse[0][3] = -dx
        inverse[1][3] = -dy
        inverse[2][3] = -dz
        return Transform(matrix, inverse)
