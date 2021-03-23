from dataclasses import dataclass
from pyrt.point import Point3
from pyrt.vec3 import Vec3
from pyrt.material import Material


@dataclass
class Intersection:
    point: Point3
    normal: Vec3
    t: float
    material: Material
