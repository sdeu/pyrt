import numpy as np
from PIL import Image
from pyrt import *

def color(ray, scene):
    return color_internal(ray, scene, 5)

def color_internal(ray, scene, depth):
    
    for shape in scene:
        hit = shape.hit(ray)
        if hit is not None:
            r = reflect(ray, hit)
            if (depth >= 0):
                return 0.5 * color_internal(r, scene, depth-1)
            else:
                return hit.material.color
            #return 0.5 * (hit.normal + Vec3(1,1,1))
            
    d = ray.direction.normalize()
    t = 0.5 * (d.y + 1.0)
    return ((1.0 - t)*Vec3(1.0, 1.0, 1.0)) + (t*Vec3(0.5, 0.7, 1.0))

def reflect(ray, intersection):
    r = ray.direction - 2 * np.dot(intersection.normal.vec[:3], ray.direction.vec[:3]) * intersection.normal
    return Ray(intersection.point, r)

def main():
    ascpect_ratio = 16.0 / 9.0
    image_width = 100
    image_height = (int)(image_width / ascpect_ratio)
    print(f'{image_width} x {image_height}')

    image = np.zeros([image_height, image_width, 3], dtype='uint8')

    scene = []
    scene.append(Sphere(1, Transform.translation(0,0,-5), SimpleMaterial(Vec3(1.0, 0.0, 0.0))))
    scene.append(Sphere(3, Transform.translation(1,-3,-10), SimpleMaterial(Vec3(0.0, 1.0, 0.0))))

    camera = Camera(image_width)

    for j in range(image_height-1, -1, -1):
        for i in range(image_width):
            u = i / (float)(image_width-1)
            v = j / (float)(image_height-1)
            ray = camera.ray(u, v)
            c = color(ray,scene)
            image[j, i] = [c.r, c.g, c.b]

    im = Image.fromarray(image, mode='RGB')
    im.save("test.jpg")

if __name__ == "__main__":
    main()