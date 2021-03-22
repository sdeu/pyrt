import io
from dataclasses import InitVar, dataclass, field
from typing import Any

import numpy as np
from PIL import Image


@dataclass
class Film:
    file_name: str
    samples: int
    width: int
    height: int
    image: Any = field(init=False)

    def __post_init__(self):
        self.image = np.zeros([self.height, self.width, 3], np.float)

    def set_pixel(self, u, v, c):
        self.image[v, u] = [c.x ** (1 / 2.2) * 255, c.y ** (1 / 2.2) * 255, c.z ** (1 / 2.2) * 255]

    def save(self):
        im = Image.fromarray(self.image.astype(np.uint8), mode='RGB')
        im.save(self.file_name)

    def as_bmp(self):
        im = Image.fromarray(self.image.astype(np.uint8), mode='RGB')
        buffer = io.BytesIO()
        im.save(buffer, format="BMP")
        return buffer.getvalue()

