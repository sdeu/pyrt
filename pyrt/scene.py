from dataclasses import dataclass
from typing import List
from pyrt.shape import Shape

@dataclass
class Scene:
    objects: List[Shape]