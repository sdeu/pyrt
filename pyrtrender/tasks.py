from .worker import app
from pyrt import *

@app.task
def render(scene, width, aspect_ratio, samples, scanlines=[]):
    height = int(width / aspect_ratio)
    print(f'{width} x {height}')

    image = Film(width, height, samples, "test.bmp")

    renderer = Renderer(width, height, samples, scene, camera, image)
    renderer.render(scanlines)
