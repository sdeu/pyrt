from pyrt import *
import jsonpickle
from celery import chord
import requests
import click

@click.command()
@click.option('--samples', default=100, help='Number of samples per pixel')
@click.option('--width', default=400, help='Width of the image')
def main(samples, width):

    aspect_ratio = 16.0 / 9.0
    width = 400
    height = int(width / aspect_ratio)

    scene = [Sphere(1, Transform.translation(1, -0.5, -5), Lambert(Vec3(1.0, 0.0, 0.0))),
             Sphere(2, Transform.translation(-2, -1.5, -5), Metal(Vec3(0.9, 0.9, 0.9))),
             Sphere(200, Transform.translation(1, 200.5, -10), Lambert(Vec3(0.0, 1.0, 0.0)))]

    camera = Camera(width)

    jscene = jsonpickle.encode(scene)
    jcamera = jsonpickle.encode(camera)

    scanlines=[]
    nlines = int(height / 8)
    for i in range(7):
        scanlines.append(list(range(i*nlines, (i+1)*nlines)))

    print(scanlines)

    callback = combine.s()
    header = [render.s(jscene, jcamera, width, aspect_ratio, samples, lines) 
    for lines in scanlines]

    result = chord(header)(callback)

    url = f'http://localhost:5001/{result.get()}'

    img_data = requests.get(url).content
    with open('test.bmp', 'wb') as handler:
        handler.write(img_data)

if __name__ == "__main__":
    main()