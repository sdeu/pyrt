from dataclasses import dataclass, field
from json import loads
from typing import Any

from dacite import Config, from_dict

from .file import File
from .transform import Translation, Transform
from .vec3 import Vec3
from .material import Lambert, Metal, Material
from .shape import Shape
from .sphere import Sphere

def transformation_from_json(t: Any) -> Any:
    if t['name'] == 'Translation':
        return Translation(*t['args'])
    raise RuntimeError('Unknown transformation type: ' + t.name)

def material_from_json(m: Any) -> Any:
    if m['name'] == 'Lambert':
        return Lambert(color=Vec3(*m['args']))
    elif m['name'] == 'Metal':
        return Metal(color=Vec3(*m['args']))
    else:
        raise RuntimeError('Unknown material type: ' + m.name)

def shape_from_json(s: Any) -> Any:
    if s['name'] == 'Sphere':
        return Sphere(
            radius=s['radius'], 
            object_to_world=transformation_from_json(s['object_to_world']), 
            material=material_from_json(s['material']))
    else:
        raise RuntimeError('Unknown shape type: ' + s.name)

type_converters = {
    Transform: transformation_from_json,
    Material: material_from_json,
    Shape: shape_from_json
}

def parse_file(f):
    with open(f, 'r') as json_file:
        lines = json_file.read()
        d = loads(lines)
        return parse_dict(d)

def parse_dict(d, data_class=File):
    return from_dict(data_class=data_class, data=d, config=Config(type_hooks=type_converters))


