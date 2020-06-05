import numpy as np
from PIL import Image
from pyrt import *
from random import uniform
from tqdm import trange
from math import pi, sqrt, cos, sin
from .worker import app

def color(ray, scene):
    return color_internal(ray, scene, 5)

def color_internal(ray, scene, depth):

    if depth < 0:
        return Vec3(0,0,0)

    for shape in scene:
        hit = shape.hit(ray)
        if hit is not None:
            if (depth >= 0):
                result = hit.material.scatter(ray, hit)
                if result is not None:
                    r,a = result
                    return a * color_internal(r, scene, depth-1)
                return Vec3(0,0,0)
            
    d = ray.direction.normalize()
    t = 0.5 * (d.y + 1.0)
    return ((1.0 - t)*Vec3(1.0, 1.0, 1.0)) + (t*Vec3(0.5, 0.7, 1.0))

@app.task
def render(scanlines=[]):
    image_width = 100
    samples = 1

    ascpect_ratio = 16.0 / 9.0
    image_height = (int)(image_width / ascpect_ratio)
    print(f'{image_width} x {image_height}')

    image = np.zeros([image_height, image_width, 3], dtype='uint8')

    scene = []
    scene.append(Sphere(1, Transform.translation(0,0,-5), Lambert(Vec3(1.0, 0.0, 0.0))))
    scene.append(Sphere(2, Transform.translation(-3,0,-5), Metal(Vec3(0.9,0.9,0.9))))
    scene.append(Sphere(200, Transform.translation(1,200.5,-10), Lambert(Vec3(0.0, 1.0, 0.0))))

    camera = Camera(image_width)

    lines = scanlines
    if len(lines) == 0:
        lines = range(image_height-1, -1, -1)

    for j in lines:
        for i in range(image_width):
            c = Vec3(0,0,0)
            for s in range(samples):
                u = (i + uniform(0, 1)) / (float)(image_width-1)
                v = (j + uniform(0, 1)) / (float)(image_height-1)
                ray = camera.ray(u, v)
                c = c + color(ray,scene)
            c = c / samples
            corrected = Vec3(c.x**(1/2.2), c.y**(1/2.2), c.z**(1/2.2))
            image[j, i] = [corrected.r, corrected.g, corrected.b]

    im = Film.fromarray(image, mode='RGB')
    im.save("test.bmp")

if __name__ == "__main__":
    render()