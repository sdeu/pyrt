from dataclasses import dataclass
from pyrt.scene import Scene
from pyrt.film import Film

@dataclass
class File:
    scene: Scene
    film: Film

