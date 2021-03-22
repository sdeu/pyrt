from dataclasses import dataclass
from scene import Scene
from film import Film

@dataclass
class File:
    scene: Scene
    film: Film

