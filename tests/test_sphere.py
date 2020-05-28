import pytest
import numpy as np
from pyrt.transform import Transform
from pyrt.point import Point3
from pyrt.vec3 import Vec3
from pyrt.ray import Ray
from pyrt.sphere import Sphere

def test_ray_intersection():
    s = Sphere(1, Transform.translation(0, 0, 0))
    ray = Ray(Point3(0, 0, 3), Vec3(0, 0, -1))
    i = s.hit(ray)
    assert i is not None
    assert i.t == 2
    assert i.point == Point3(0,0,1)
    assert i.normal == Vec3(0,0,1)

def test_ray_intersection_miss():
    s = Sphere(1, Transform.translation(0, 0, 0))
    ray = Ray(Point3(0, 0, 3), Vec3(0, 1, 0))
    assert s.hit(ray) is None