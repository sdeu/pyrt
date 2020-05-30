from abc import ABC, abstractmethod
from random import uniform
from math import pi, sqrt, cos, sin
from .vec3 import Vec3
from .ray import Ray

class Material(ABC):

    @abstractmethod
    def scatter(self, ray, intersection):
        pass

def random_unit_vector():
        a = uniform(0, 2*pi)
        z = uniform(-1, 1)
        r = sqrt(1 - z*z)
        return Vec3(r*cos(a), r* sin(a), z)

class Lambert(Material):
    
    def __init__(self, color):
        self.__color = color

    def scatter(self, ray, intersection):
        r = intersection.normal + random_unit_vector()
        return Ray(intersection.point + (intersection.normal*0.001), r), self.__color