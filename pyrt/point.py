from dataclasses import InitVar, dataclass, field
from typing import Any

import numpy as np

from pyrt.vec3 import Vec3


@dataclass
class Point3:
    x: InitVar[float]
    y: InitVar[float]
    z: InitVar[float]
    vec: Any = None
    
    def __post_init__(self, px, py, pz):
        if self.vec is None:
            self.vec = np.array([px, py, pz, 1])

    def __add__(self, other):
        if isinstance(other, Point3):
            return Vec3(vec=self.vec + other.vec)
        if isinstance(other, Vec3):
            return Point3(vec=self.vec + other.vec)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Point3):
            return Vec3(vec=self.vec + other.vec)
        if isinstance(other, Vec3):
            return Point3(vec=self.vec + other.vec)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vec3(vec=self.vec - other.vec)
        if isinstance(other, Vec3):
            return Point3(vec=self.vec - other.vec)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Point3):
            return Vec3(vec=self.vec - other.vec)
        if isinstance(other, Vec3):
            return Point3(vec=self.vec - other.vec)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point3):
            return np.array_equal(self.vec, other.vec)
        return NotImplemented

    def __hash__(self):
        return hash(self.vec)

    @property
    def x(self):
        return self.vec[0]
    
    @property
    def y(self):
        return self.vec[1]

    @property
    def z(self):
        return self.vec[2]

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
