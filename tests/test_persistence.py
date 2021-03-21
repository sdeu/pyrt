from pyrt.transform import Translation, Transform
from pyrt.parser import parse_dict
from pyrt.material import Material
from pyrt.sphere import Sphere


def test_sphere():
    d = {
        "radius": 42,
        "object_to_world": {"name": "Translation", "args": [1, 2, 3]},
        "material": {"name": "Lambert", "args": [1, 2, 3]}
        }
    
    s = parse_dict(d, data_class=Sphere)
    assert s is not None
    assert s.radius == 42
    assert s.object_to_world.matrix[0][3] == 1
    assert s.object_to_world.matrix[1][3] == 2
    assert s.object_to_world.matrix[2][3] == 3
    assert s.material.color.r == 255