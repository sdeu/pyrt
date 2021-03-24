from dataclasses import dataclass, field
from math import sqrt

import numpy as np

from pyrt.intersection import Intersection
from pyrt.material import Material
from pyrt.shape import Shape
from pyrt.transform import Transform
from pyrt.vec3 import Vec3


@dataclass
class Sphere(Shape):
    radius: float
    object_to_world: Transform
    material: Material
    world_to_object: Transform = field(init=False)

    def __post_init__(self):
        self.world_to_object = self.object_to_world.inverse

    def hit(self, ray):
        r = self.world_to_object @ ray
        t = self.__hit_internal(
            r.direction.vec[:3], r.origin.vec[:3], self.radius)

        if t is not None:
            intersection_point = r.point_at(t)
            return Intersection(self.object_to_world @ intersection_point,
                                Vec3(vec=intersection_point.vec).normalize(), t, self.material)
        return None

    def __hit_internal(self, direction, origin, radius):
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
