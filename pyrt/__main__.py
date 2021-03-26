"""Console script for pyrt."""
import sys

print(sys.path)

import click
from pyrt.camera import Camera
from pyrt.render import Renderer
from pyrt.parser import parse_file


@click.command()
@click.argument('filepath')
@click.option('--nprocs', default=8)
@click.option('--chunksize', default=4)
def main(filepath, nprocs, chunksize):

    f = parse_file(filepath)
    camera = Camera(f.film.width)
    renderer = Renderer(width=f.film.width, height=f.film.height,
                        samples=f.film.samples, scene=f.scene, camera=camera, film=f.film)
    renderer.render(nprocs, chunksize)
    f.film.save()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
