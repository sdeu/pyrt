from dataclasses import dataclass
from random import uniform

import numpy as np

from pyrt.camera import Camera
from pyrt.film import Film
from pyrt.scene import Scene
from pyrt.vec3 import Vec3
from pyrt.timing import timing

from tqdm.contrib.concurrent import process_map

def _chunks(nlines, n):
    for i in range(0, nlines, n):
        yield (i, list(range(min(n, nlines-i))))

sky = np.array([0.5, 0.7, 1.0])
zero = np.zeros([1,3])
one = np.ones([1,3])

@dataclass
class Renderer:
    film: Film
    camera: Camera
    scene: Scene
    samples: int
    height: int
    width: int

    @timing
    def render(self, nproc, chunksize):
        print(f'width = {self.width}')
        print(f'height = {self.height}')
        print(f'samples = {self.samples}')
        images = {}
        if nproc != 0:
            images = sorted(process_map(self._render_lines, list(_chunks(self.height, chunksize)), max_workers=nproc), key=lambda i:i[0])
        else:
            images = list(self._render_lines((0, list(range(self.height)))))
        img = np.concatenate([i[1] for i in images], axis=1)
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                self.film.set_pixel(i, j, Vec3(x=img[i,j, 0], y=img[i, j, 1], z=img[i, j, 2]))

    def _render_lines(self, data: tuple) -> np.ndarray:
        offset, lines = data[0], data[1]
        image = np.zeros([self.width, len(lines), self.samples, 3], float)
        for j in lines:
            for i in range(self.width):
                for s in range(self.samples):
                    u = (i + uniform(0, 1)) / float(self.width - 1)
                    v = (j + offset + uniform(0, 1)) / float(self.height - 1)
                    ray = self.camera.ray(u, v)
                    image[i, j, s] = color(ray, self.scene)
        image = image.sum(axis=2) / self.samples
        return (offset, image)
        
def color(ray, scene):
    return color_internal(ray, scene.objects, 5)


def color_internal(ray, scene, depth):
    if depth < 0:
        return zero

    hits = list(filter(None, map(lambda s: s.hit(ray), scene)))
    if len(hits) > 0:
        hit = min(hits, key=lambda h: h.t)
        if depth >= 0:
            result = hit.material.scatter(ray, hit)
            if result is not None:
                r, a = result
                return a.vec[0:3] * color_internal(r, scene, depth - 1)
            return zero

    d = ray.direction.normalize()
    t = 0.5 * (d.y + 1.0)
    return ((1.0 - t) * one) + (t * sky)
