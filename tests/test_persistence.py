from dacite import from_dict
from pyrt.transform import Translation

def test_transformation():
    d = {"dx": 1, "dy": 2, "dz": 3}
    t = from_dict(data_class=Translation, data=d)
    assert t is not None
    assert t.matrix[0][3] == 1
    assert t.matrix[1][3] == 2
    assert t.matrix[2][3] == 3