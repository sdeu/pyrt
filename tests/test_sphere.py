import pytest
import numpy as np
from pyrt.transform import Transform
from pyrt.point import Point3
from pyrt.vec3 import Vec3
from pyrt.ray import Ray
from pyrt.sphere import Sphere

def test_ray_intersection():
    s = Sphere(1, Transform.translation(0, 0, 0))

    ray1 = Ray(Point3(0, 0, 3), Vec3(0, 0, -1))
    assert s.hit(ray1) == 2

    ray2 = Ray(Point3(0, 0, 3), Vec3(0, 1, 0))
    assert s.hit(ray2) is None

    ray3 = Ray(Point3(0,0,3), Vec3(0, 0, 1))
    assert s.hit(ray3) is None

    ray4 = Ray(Point3(0,0,3), Vec3(1.2873563218390802,0.33333333333333326,-1.0))
    s2 = Sphere(10, Transform.translation(0, 0, 0))
    assert s2.hit(ray4) is not None