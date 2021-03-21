from dataclasses import dataclass, field
from typing import Any

from .vec3 import Vec3


@dataclass
class Scene:
    objects: list

@dataclass
class Translation:
    dx: float
    dy: float
    dz: float


@dataclass
class MaterialLambert:
    material_type: str = field(default='Lambert', init=False)
    r: float
    g: float
    b: float

@dataclass
class MaterialMetal:
    material_type: str = field(default='Metal', init=False)
    r: float
    g: float
    b: float


@dataclass
class SceneObject:
    object_type: str
    transformations: list
    material: Any

@dataclass
class SceneFilm:
    width: int 
    height: int 
    samples: int 
    file_name: str


@dataclass
class File:
    film: SceneFilm
    scene: Scene

