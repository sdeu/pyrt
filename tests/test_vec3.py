from pyrt.vec3 import Vec3
import numpy as np

def test_creation_elementwise():
    v = Vec3(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3
    assert v.vec[-1] == 0

def test_creation_from_vec():
    v = Vec3(vec=[1, 2, 3, 0])
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3
    assert v.vec[-1] == 0