"""Console script for pyrt."""
import sys
import click
from .film import Film
from .sphere import Sphere
from .transform import Translation
from .material import Lambert, Metal
from .vec3 import Vec3
from .camera import Camera
from .render import Renderer
from .scene import Scene
from .parser import parse_file


@click.command()
@click.argument('filepath')
def main(filepath):

    f = parse_file(filepath)
    camera = Camera(f.film.width)
    renderer = Renderer(width=f.film.width, height=f.film.height,
                        samples=f.film.samples, scene=f.scene, camera=camera, film=f.film)
    renderer.render()
    f.film.save()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
