from PIL import Image
import numpy as np
import io

class Film:
    def __init__(self, width, height, samples, file_name):
        self.file_name = file_name
        self.samples = samples
        self.__image = np.zeros([height, width, 4], np.float)
        #self.__image[:,:,3] = 1.0

    def set_pixel(self, u, v, c):
        self.__image[v, u] = [c.x ** (1 / 2.2) * 255, c.y ** (1 / 2.2) * 255, c.z ** (1 / 2.2) * 255, 0.0]

    def save(self):
        im = Image.fromarray(self.__image.astype(np.uint8), mode='RGBA')
        im.save(self.file_name)

    def as_bmp(self):
        im = Image.fromarray(self.__image.astype(np.uint8), mode='RGBA')
        buffer = io.BytesIO()
        im.save(buffer, format="PNG")
        return buffer.getvalue()

