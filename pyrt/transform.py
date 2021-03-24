from typing import Any
import numpy as np
from pyrt.vec3 import Vec3
from pyrt.point import Point3
from pyrt.ray import Ray
from dataclasses import dataclass, InitVar, field
from abc import ABC

@dataclass
class Transform(ABC):
    matrix: Any = field(init=False)
    inverse_matrix: Any = field(init=False)

    @property
    def inverse(self):
        if self.inverse_matrix is not None:
            t = Transform()
            t.matrix, t.inverse_matrix = self.inverse_matrix, self.matrix
            return t

        inv = np.linalg.inv(self.matrix)
        t = Transform()
        t.matrix, t.inverse_matrix = inv, self.matrix
        return t

    def __matmul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(vec=self.matrix @ other.vec)

        if isinstance(other, Point3):
            return Point3(vec=self.matrix @ other.vec)

        if isinstance(other, Ray):
            return Ray(Point3(vec=self.matrix @ other.origin.vec),
                       Vec3(vec=self.matrix @ other.direction.vec))

@dataclass
class Translation(Transform):
    dx: InitVar[float]
    dy: InitVar[float]
    dz: InitVar[float]

    def __post_init__(self, dx, dy, dz):
        self.matrix = np.identity(4)
        self.matrix[0][3] = dx
        self.matrix[1][3] = dy
        self.matrix[2][3] = dz

        self.inverse_matrix = np.identity(4)
        self.inverse_matrix[0][3] = -dx
        self.inverse_matrix[1][3] = -dy
        self.inverse_matrix[2][3] = -dz
