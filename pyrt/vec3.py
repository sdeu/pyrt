import numpy as np

class Vec3:
    def __init__(self, x, y, z):
        self.__vec = np.array([x,y,z], dtype=np.float)

    @property
    def vec(self):
        return self.__vec

    @classmethod
    def from_array(cls, v):
        return Vec3(v[0], v[1], v[2])

    def __add__(self, other):
        return Vec3.from_array(self.__vec + other.__vec)

    def __sub__(self, other):
        return Vec3.from_array(self.__vec - other.__vec)

    def __mul__(self, other):
        return Vec3.from_array(self.__vec * other)

    def __rmul__(self, other):
        return Vec3.from_array(self.__vec * other)

    def __truediv__(self, other):
        return Vec3.from_array(self.__vec / other)

    def normalize(self):
        return Vec3.from_array(self.__vec / np.linalg.norm(self.__vec))

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