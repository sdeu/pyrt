import numpy as np
from PIL import Image
from pyrt import *

def color(ray, scene):
    for shape in scene:
        hit = shape.hit(ray)
        if hit is not None:
            return 0.5 * (hit.normal + Vec3(1,1,1))
            
    d = ray.direction.normalize()
    t = 0.5 * (d.y + 1.0)
    return ((1.0 - t)*Vec3(1.0, 1.0, 1.0)) + (t*Vec3(0.5, 0.7, 1.0))

def main():
    ascpect_ratio = 16.0 / 9.0
    image_width = 800
    image_height = (int)(image_width / ascpect_ratio)
    print(f'{image_width} x {image_height}')

    image = np.zeros([image_height, image_width, 3], dtype='uint8')

    viewport_height = 2.0
    viewport_width = ascpect_ratio * viewport_height

    focal_length = 1.0

    origin = Point3(0,0,0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)

    lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(0,0,focal_length)

    scene = []
    scene.append(Sphere(1, Transform.translation(0,0,-5)))
    scene.append(Sphere(3, Transform.translation(1,-3,-10)))

    for j in range(image_height-1, -1, -1):
        for i in range(image_width):
            u = i / (float)(image_width-1)
            v = j / (float)(image_height-1)
            ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
            c = color(ray,scene)
            image[j, i] = [c.r, c.g, c.b]

    im = Image.fromarray(image, mode='RGB')
    im.save("test.jpg")

if __name__ == "__main__":
    main()