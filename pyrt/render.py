from random import uniform
from tqdm import trange
from .vec3 import Vec3


class Renderer:
    def __init__(self, width, height, samples, scene, camera, film):
        self.film = film
        self.camera = camera
        self.scene = scene
        self.sample = samples
        self.height = height
        self.width = width

    def render(self):
        for j in trange(self.height - 1, -1, -1):
            for i in range(self.width):
                c = Vec3(0, 0, 0)
                for s in range(self.sample):
                    u = (i + uniform(0, 1)) / float(self.width - 1)
                    v = (j + uniform(0, 1)) / float(self.height - 1)
                    ray = self.camera.ray(u, v)
                    c = c + color(ray, self.scene)
                self.film.set_pixel(i, j, c)

        self.film.save()


def color(ray, scene):
    return color_internal(ray, scene, 5)


def color_internal(ray, scene, depth):
    if depth < 0:
        return Vec3(0, 0, 0)

    for shape in scene:
        hit = shape.hit(ray)
        if hit is not None:
            if depth >= 0:
                result = hit.material.scatter(ray, hit)
                if result is not None:
                    r, a = result
                    return a * color_internal(r, scene, depth - 1)
                return Vec3(0, 0, 0)

    d = ray.direction.normalize()
    t = 0.5 * (d.y + 1.0)
    return ((1.0 - t) * Vec3(1.0, 1.0, 1.0)) + (t * Vec3(0.5, 0.7, 1.0))