import pytest
from pyrt.transform import Transform
from pyrt.point import Point3
from pyrt.vec3 import Vec3

def test_translat_point():
    p = Point3(1, 1, 1)
    m = Transform.translation(1, 2, 3)
    t = m @ p
    assert t.x == 2
    assert t.y == 3
    assert t.z == 4