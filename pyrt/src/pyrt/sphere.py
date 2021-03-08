from dataclasses import dataclass
import numpy as np
from math import sqrt
from .shape import Shape
from .intersection import Intersection
from .vec3 import Vec3
from .transform import Transform
from .material import Material


@dataclass
class Sphere(Shape):
    __radius: float
    __object_to_world: Transform
    __world_to_object: Transform
    __material: Material

    def hit(self, ray):
        r = self.__world_to_object @ ray
        t = __hit_internal(r.direction.vec[:3], r.origin.vec[:3], self.__radius)

        if t is not None:
            intersection_point = r.point_at(t)
            return Intersection(self.__object_to_world @ intersection_point,
                                Vec3.from_array(intersection_point.vec).normalize(), t, self.__material)
        return None


def __hit_internal(direction, origin, radius):
    A = np.dot(direction, direction)
    B = 2 * np.dot(origin, direction)
    C = np.dot(origin, origin) - radius ** 2

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

