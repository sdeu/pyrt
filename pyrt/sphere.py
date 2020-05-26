import numpy as np
from .shape import Shape
from .ray import Ray

class Sphere(Shape):
    def __init__(self, radius, transformation):
        self.__radius = radius
        self.__object_to_world = transformation
        self.__world_to_object = transformation.inverse

    def hit(self, ray):
        r = self.__world_to_object @ ray
        A = np.dot(r.direction.vec[:3], r.direction.vec[:3])
        B = 2 * np.dot(r.origin.vec[:3], r.direction.vec[:3])
        C = np.dot(r.origin.vec[:3], r.origin.vec[:3]) - self.__radius**2
        roots = np.roots([A,B,C])

        return np.amin(roots.real) if roots is not None else None