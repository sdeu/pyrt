import os
from .worker import app
from .film import Film
from .render import Renderer
import jsonpickle
import requests
from PIL import Image
import io
import numpy as np

STORAGE_HOST = os.getenv('STORAGE_HOST')
STORAGE_PORT = os.getenv('STORAGE_PORT')

@app.task(name="render")
def render(scene, camera, width, aspect_ratio, samples, scanlines=[]):
    decoded_scene = jsonpickle.decode(scene)
    decoded_camera = jsonpickle.decode(camera)
    return render_internal(decoded_scene, decoded_camera, width, aspect_ratio, samples, scanlines)

@app.task(name="combine")
def combine(images):
    image = None
    for f in images:
        url = f'http://{STORAGE_HOST}:{STORAGE_PORT}/{f}'

        r = requests.get(url)
        im = Image.open(io.BytesIO(r.content))

        if image is None:
            image = np.array(im)
        else:
            image = image + np.array(im)
    
    buffer = io.BytesIO()
    im = Image.fromarray(image.astype(np.uint8), mode='RGB')
    im.save(buffer, format="bmp")

    url = f'http://{STORAGE_HOST}:{STORAGE_PORT}/combined_{combine.request.id}'
    x = requests.post(url, files={'file':buffer.getvalue()})

    print(f"Combined image: combined_{combine.request.id}")


def render_internal(scene, camera, width, aspect_ratio, samples, scanlines=[]):
    height = int(width / aspect_ratio)
    print(f'{width} x {height}')

    image = Film(width, height, samples, "test.bmp")

    renderer = Renderer(width, height, samples, scene, camera, image)
    renderer.render(scanlines)

    url = f'http://{STORAGE_HOST}:{STORAGE_PORT}/{render.request.id}'
    x = requests.post(url, files={'file':renderer.film.as_bmp()})
    return render.request.id

