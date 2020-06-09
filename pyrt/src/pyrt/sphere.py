import numpy as np
from math import sqrt
from .shape import Shape
from .intersection import Intersection
from .vec3 import Vec3


class Sphere(Shape):
    def __init__(self, radius, transformation, material):
        self.__radius = radius
        self.__object_to_world = transformation
        self.__world_to_object = transformation.inverse
        self.__material = material

    def hit(self, ray):
        r = self.__world_to_object @ ray
        t = self.__hit_internal(r)

        if t is not None:
            intersection_point = r.point_at(t)
            return Intersection(self.__object_to_world @ intersection_point,
                                Vec3.from_array(intersection_point.vec).normalize(), t, self.__material)
        return None


    def __hit_internal(self, r):
        A = np.dot(r.direction.vec[:3], r.direction.vec[:3])
        B = 2 * np.dot(r.origin.vec[:3], r.direction.vec[:3])
        C = np.dot(r.origin.vec[:3], r.origin.vec[:3]) - self.__radius ** 2

        d = B ** 2 - 4 * A * C

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

        t = min(t0, t1)

        if t0 < 0 and t1 > 0:
            t = t1

        if t1 < 0 and t0 > 0:
            t = t0

        return t

        # roots = np.roots([A,B,C])
        # if roots is not None:
        #     positive_roots = np.where(roots.real >= 0)
        #     if len(positive_roots) > 0:
        #         return np.amin(positive_roots)

        # return None