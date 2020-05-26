import pytest
import numpy as np
from pyrt.transform import Transform
from pyrt.point import Point3
from pyrt.vec3 import Vec3
from pyrt.ray import Ray

def test_translate_point():
    p = Point3(1, 1, 1)
    m = Transform.translation(1, 2, 3)
    t = m @ p
    assert t.x == 2
    assert t.y == 3
    assert t.z == 4

def test_translate_vector():
    v = Vec3(1, 1, 1)
    m = Transform.translation(1, 2, 3)
    t = m @ v
    assert np.array_equal(t.vec, np.array([1.0, 1.0, 1.0, 0.0]))

def test_translate_ray():
    r = Ray(Point3(0, 0, 0), Vec3(0, 0, -1))
    m = Transform.translation(1, 2, 3)
    t = m @ r
    assert np.array_equal(t.origin.vec, np.array([1.0, 2.0, 3.0, 1.0]))
    assert np.array_equal(t.direction.vec, np.array([0.0, 0.0, -1.0, 0.0]))