from dataclasses import InitVar, dataclass, field
from math import sqrt
from typing import Any

import numpy as np


@dataclass
class Vec3:
    __vec: Any = field(init=False)
    x: InitVar[float]
    y: InitVar[float]
    z: InitVar[float]
    
    def __post_init__(self, px, py, pz):
        self.__vec = np.array([px, py, pz, 0])

    @property
    def vec(self):
        return self.__vec

    @classmethod
    def from_array(cls, v):
        return Vec3(v[0], v[1], v[2])

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.vec + other.__vec)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.vec - other.__vec)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.vec * other.__vec)
        return Vec3.from_array(self.__vec * other)

    def __rmul__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.vec * other.__vec)
        return Vec3.from_array(self.__vec * other)

    def __truediv__(self, other):
        return Vec3.from_array(self.__vec / other)

    def __eq__(self, other):
        if isinstance(other, Vec3):
            return np.array_equal(self.__vec, other.__vec)
        return NotImplemented

    def __hash__(self):
        return hash(self.__vec)

    def normalize(self):
        return Vec3.from_array(self.vec / sqrt(self.length_2))

    @property
    def x(self):
        return self.__vec[0]

    @property
    def y(self):
        return self.__vec[1]

    @property
    def z(self):
        return self.__vec[2]

    @property
    def r(self):
        return (int)(self.x * 255.0)

    @property
    def g(self):
        return (int)(self.y * 255.0)

    @property
    def b(self):
        return (int)(self.z * 255.0)

    @property
    def length_2(self):
        return self.__vec[0]**2 + self.__vec[1]**2 + self.__vec[2]**2

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
