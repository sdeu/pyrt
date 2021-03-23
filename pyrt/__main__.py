"""Console script for pyrt."""
import sys

print(sys.path)

import click
from pyrt.camera import Camera
from pyrt.render import Renderer
from pyrt.parser import parse_file


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
