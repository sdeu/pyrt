from .pyrt import *


def main():
    image_width = 400
    samples = 60

    aspect_ratio = 16.0 / 9.0
    image_height = int(image_width / aspect_ratio)
    print(f'{image_width} x {image_height}')

    image = Film(image_width, image_height, samples, "test.bmp")

    scene = [Sphere(1, Transform.translation(0, 0, -5), Lambert(Vec3(1.0, 0.0, 0.0))),
             Sphere(2, Transform.translation(-3, 0, -5), Metal(Vec3(0.9, 0.9, 0.9))),
             Sphere(200, Transform.translation(1, 200.5, -10), Lambert(Vec3(0.0, 1.0, 0.0)))]

    camera = Camera(image_width)

    renderer = Renderer(image_width, image_height, samples, scene, camera, image)
    renderer.render()


if __name__ == "__main__":
    main()
