import numpy as np
from .vec3 import Vec3
from .point import Point3

class Transform():
    def __init__(self, matrix, inverse=None):
        self.__matrix = matrix
        self.__inverse = inverse

    @classmethod
    def translation(cls, dx, dy, dz):
        matrix = np.identity(4)
        matrix[0][3] = dx
        matrix[1][3] = dy
        matrix[2][3] = dz
        return Transform(matrix)

    def __matmul__(self, other):
        if isinstance(other, Vec3):
            return Vec3.from_array(self.__matrix @ other.vec)

        if isinstance(other, Point3):
            return Point3.from_array(self.__matrix @ other.vec)

    
