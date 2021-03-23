from dataclasses import InitVar, dataclass, field
from typing import Any

import numpy as np

from pyrt.vec3 import Vec3


@dataclass
class Point3:
    __vec: Any = field(init=False)
    x: InitVar[float]
    y: InitVar[float]
    z: InitVar[float]
    
    def __post_init__(self, px, py, pz):
        self.__vec = np.array([px, py, pz, 1])

    @classmethod
    def from_array(cls, p):
        return Point3(p[0], p[1], p[2])

    @property
    def vec(self):
        return self.__vec

    def __add__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec + other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec + other.vec)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec + other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec + other.vec)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec - other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec - other.vec)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec - other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec - other.vec)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point3):
            return np.array_equal(self.__vec, other.vec)
        return NotImplemented

    def __hash__(self):
        return hash(self.__vec)

    @property
    def x(self):
        return self.__vec[0]
    
    @property
    def y(self):
        return self.__vec[1]

    @property
    def z(self):
        return self.__vec[2]

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
