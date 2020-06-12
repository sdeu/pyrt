from pyrt import *
import jsonpickle
from celery import chord

def main():

    aspect_ratio = 16.0 / 9.0
    image_width = 100
    height = int(image_width / aspect_ratio)
    samples = 10

    scene = [Sphere(1, Transform.translation(1, -0.5, -5), Lambert(Vec3(1.0, 0.0, 0.0))),
             Sphere(2, Transform.translation(-2, -1.5, -5), Metal(Vec3(0.9, 0.9, 0.9))),
             Sphere(200, Transform.translation(1, 200.5, -10), Lambert(Vec3(0.0, 1.0, 0.0)))]

    camera = Camera(image_width)

    jscene = jsonpickle.encode(scene)
    jcamera = jsonpickle.encode(camera)

    scanlines=[]
    nlines = int(height / 8)
    for i in range(7):
        scanlines.append(list(range(i*nlines, (i+1)*nlines)))

    print(scanlines)

    # chord(render.s(jscene, jcamera, image_width, aspect_ratio, samples, lines) 
    # for lines in scanlines)(combine.s()).get()
    
    #render.delay(jsonpickle.encode(scene), jsonpickle.encode(camera), image_width, aspect_ratio, samples)

if __name__ == "__main__":
    main()