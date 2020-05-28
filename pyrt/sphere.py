import numpy as np
from math import sqrt
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

        root_d = sqrt(d)

        q = 1
        if B < 0:
            q = -0.5 * (B - root_d)
        else:
            q = -0.5 * (B + root_d)

        t0 = q / A
        t1 = C / q

        if t1 < 0 and t0 < 0:
            return None

        if t0 < 0 and t1 > 0:
            return t1

        if t1 < 0 and t0 > 0:
            return t0
        
        return min(t0, t1)
        # roots = np.roots([A,B,C])
        # if roots is not None:
        #     positive_roots = np.where(roots.real >= 0)
        #     if len(positive_roots) > 0:
        #         return np.amin(positive_roots)

        # return None