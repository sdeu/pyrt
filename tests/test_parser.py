from pyrt.parser import *
from jsonpickle import encode
from dataclasses import asdict
from dacite import from_dict

def test_foo_bar():

    film = SceneFilm(width=10, height=20, samples=30, file_name='test.bmp')
    
    metal = MaterialMetal(r=1.0, g=2.0, b=3.0)
    translation = Translation(11.0, 12.0, 13.0)
    sphere = SceneObject('Sphere', transformations=[translation], material=metal)
    scene = Scene([sphere])

    f = File(film, scene)

    d = asdict(f)
    restored = from_dict(data_class=File, data=d)
    
    print(restored)
    assert True