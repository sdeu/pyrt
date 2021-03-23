from dataclasses import dataclass
from random import seed, uniform

from tqdm import tqdm

from pyrt.camera import Camera
from pyrt.film import Film
from pyrt.scene import Scene
from pyrt.vec3 import Vec3


@dataclass
class Renderer:
    film: Film
    camera: Camera
    scene: Scene
    samples: int
    height: int
    width: int

    def render(self, scanlines=[]):
        print(f'width = {self.width}')
        print(f'height = {self.height}')
        print(f'samples = {self.samples}')
        lines = scanlines
        if len(lines) == 0:
            lines = range(self.height - 1, -1, -1)
        t = tqdm(total=len(lines)*self.width*self.samples, unit='samples')
        for j in lines:
            for i in range(self.width):
                c = Vec3(0, 0, 0)
                for s in range(self.samples):
                    u = (i + uniform(0, 1)) / float(self.width - 1)
                    v = (j + uniform(0, 1)) / float(self.height - 1)
                    ray = self.camera.ray(u, v)
                    c = c + color(ray, self.scene)
                    t.update()
                self.film.set_pixel(i, j, c / self.samples)
        t.close()


def color(ray, scene):
    return color_internal(ray, scene.objects, 5)


def color_internal(ray, scene, depth):
    if depth < 0:
        return Vec3(0, 0, 0)

    hits = list(filter(None, map(lambda s: s.hit(ray), scene)))
    if len(hits) > 0:
        hit = min(hits, key=lambda h: h.t)
        if depth >= 0:
            result = hit.material.scatter(ray, hit)
            if result is not None:
                r, a = result
                return a * color_internal(r, scene, depth - 1)
            return Vec3(0, 0, 0)

    d = ray.direction.normalize()
    t = 0.5 * (d.y + 1.0)
    return ((1.0 - t) * Vec3(1.0, 1.0, 1.0)) + (t * Vec3(0.5, 0.7, 1.0))
