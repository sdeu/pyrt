import numpy as np

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
        return Point3.from_array(self.__vec + other.__vec)

    def __sub__(self, other):
        return Point3.from_array(self.__vec - other.__vec)

    def __mul__(self, other):
        return Point3.from_array(self.__vec * other)

    def __rmul__(self, other):
        return Point3.from_array(self.__vec * other)

    def __truediv__(self, other):
        return Point3.from_array(self.__vec / other)

    def normalize(self):
        return Point3.from_array(self.__vec / np.linalg.norm(self.__vec[:3]))

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