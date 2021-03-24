from dataclasses import InitVar, dataclass, field
from math import sqrt
from typing import Any

import numpy as np


@dataclass
class Vec3:
    x: InitVar[float]
    y: InitVar[float]
    z: InitVar[float]
    vec: Any = None
    
    def __post_init__(self, px, py, pz):
        if self.vec is None:
            self.vec = np.array([px, py, pz, 0])
        else:
            self.vec[-1] = 0

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(vec=np.add(self.vec, other.vec))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(vec=np.subtract(self.vec, other.vec))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(vec=np.multiply(self.vec, other.vec))
        return Vec3(vec=np.multiply(self.vec, other))

    def __rmul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(vec=np.multiply(self.vec, other.vec))
        return Vec3(vec=np.multiply(self.vec, other))

    def __truediv__(self, other):
        return Vec3(vec=np.divide(self.vec, other))

    def __eq__(self, other):
        if isinstance(other, Vec3):
            return np.array_equal(self.vec, other.vec)
        return NotImplemented

    def __hash__(self):
        return hash(self.vec)

    def normalize(self):
        return Vec3(vec=np.divide(self.vec, sqrt(self.length_2)))

    @property
    def x(self):
        return self.vec[0]

    @property
    def y(self):
        return self.vec[1]

    @property
    def z(self):
        return self.vec[2]

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
        return self.vec[0]**2 + self.vec[1]**2 + self.vec[2]**2

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
