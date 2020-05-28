import numpy as np

class Vec3:
    def __init__(self, x, y, z):
        self.__vec = np.array([x,y,z,0], dtype=np.float)

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
        return Vec3.from_array(self.__vec * other)

    def __rmul__(self, other):
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
        return Vec3.from_array(self.vec / np.linalg.norm(self.vec[:3]))

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

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'