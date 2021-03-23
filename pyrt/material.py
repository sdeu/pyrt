from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import cos, pi, sin, sqrt
from random import uniform

import numpy as np

from pyrt.ray import Ray
from pyrt.vec3 import Vec3


class Material(ABC):

    @abstractmethod
    def scatter(self, ray, intersection):
        pass


def random_unit_vector():
    a = uniform(0, 2 * pi)
    z = uniform(-1, 1)
    r = sqrt(1 - z * z)
    return Vec3(r * cos(a), r * sin(a), z)


def reflect(ray, intersection):
    r_n = ray.direction.normalize()
    r = r_n - \
        ((2 * np.dot(intersection.normal.vec[:3],
         r_n.vec[:3])) * intersection.normal)
    return Ray(intersection.point, r)


@dataclass
class Lambert(Material):
    color: Vec3

    def scatter(self, ray, intersection):
        r = intersection.normal + random_unit_vector()
        return Ray(intersection.point + (intersection.normal * 0.001), r), self.color


@dataclass
class Metal(Material):
    color: Vec3

    def scatter(self, ray, intersection):
        r = reflect(ray, intersection)
        if np.dot(r.direction.vec[:3], intersection.normal.vec[:3]) > 0:
            return r, self.color
        return None
