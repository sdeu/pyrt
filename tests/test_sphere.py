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

    ray2 = Ray(Point3(0,0,3), Vec3(0, 0, 1))
    assert s.hit(ray2) is None