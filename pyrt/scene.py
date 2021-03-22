from dataclasses import dataclass
from typing import List
from shape import Shape

@dataclass
class Scene:
    objects: List[Shape]