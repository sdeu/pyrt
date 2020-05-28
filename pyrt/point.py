import numpy as np
from .vec3 import Vec3

class Point3:
    def __init__(self, x, y, z):
        self.__vec = np.array([x,y,z, 1], dtype=np.float)

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
        raise TypeError(type(other))

    def __radd__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec + other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec + other.vec)
        raise TypeError(type(other))

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec - other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec - other.vec)
        raise TypeError(type(other))

    def __rsub__(self, other):
        if isinstance(other, Point3):
            return Vec3.from_array(self.vec - other.vec)
        if isinstance(other, Vec3):
            return Point3.from_array(self.vec - other.vec)
        raise TypeError(type(other))

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