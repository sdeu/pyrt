"""Console script for pyrt."""
import sys
import click
from .film import Film
from .sphere import Sphere
from .transform import Transform
from .material import Lambert, Metal
from .vec3 import Vec3
from .camera import Camera
from .render import Renderer


@click.command()
def main(args=None):
    image_width = 100
    samples = 10

    aspect_ratio = 16.0 / 9.0
    image_height = int(image_width / aspect_ratio)
    print(f'{image_width} x {image_height}')

    image = Film(image_width, image_height, samples, "test.bmp")

    scene = [Sphere(1, Transform.translation(1, -0.5, -5), Lambert(Vec3(1.0, 0.0, 0.0))),
             Sphere(2, Transform.translation(-2, -1.5, -5),
                    Metal(Vec3(0.9, 0.9, 0.9))),
             Sphere(200, Transform.translation(1, 200.5, -10), Lambert(Vec3(0.0, 1.0, 0.0)))]

    camera = Camera(image_width)

    renderer = Renderer(width=image_width, height=image_height,
                        samples=samples, scene=scene, camera=camera, film=image)
    renderer.render()
    image.save()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
