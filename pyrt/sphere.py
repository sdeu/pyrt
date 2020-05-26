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

        d = B**2-4*A*C 

        if d < 0:
            return None

        roots = np.roots([A,B,C])

        test = np.amin(np.where(roots.real >= 0)) if roots is not None else None
        if roots is not None and np.amin(roots.real) >= 0:
            return np.amin(roots.real)

        return None