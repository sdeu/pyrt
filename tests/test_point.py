from pyrt.point import Point3
from pyrt.vec3 import Vec3


def test_point_point_addition():
    assert isinstance(Point3(0, 0, 0) + Point3(0, 0, 0), Vec3)


def test_point_vec_addition():
    assert isinstance(Point3(0, 0, 0) + Vec3(0, 0, 0), Point3)
    assert isinstance(Vec3(0, 0, 0) + Point3(0, 0, 0), Point3)
