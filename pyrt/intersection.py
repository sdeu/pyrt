from dataclasses import dataclass
from point import Point3
from vec3 import Vec3
from material import Material


@dataclass
class Intersection:
    point: Point3
    normal: Vec3
    t: float
    material: Material
