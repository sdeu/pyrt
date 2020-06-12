from PIL import Image
import numpy as np
import io

class Film:
    def __init__(self, width, height, samples, file_name):
        self.file_name = file_name
        self.samples = samples
        self.__image = np.zeros([height, width, 3], np.float)

    def set_pixel(self, u, v, c):
        self.__image[v, u] = [c.x, c.y, c.z]

    def save(self):
        tmp_img = ((self.__image / self.samples) ** (1 / 2.2)) * 255
        im = Image.fromarray(tmp_img.astype(np.uint8), mode='RGB')
        im.save(self.file_name)

    def as_bmp(self):
        tmp_img = ((self.__image / self.samples) ** (1 / 2.2)) * 255
        im = Image.fromarray(tmp_img.astype(np.uint8), mode='RGB')
        buffer = io.BytesIO()
        im.save(buffer, format="BMP")
        return buffer.getvalue()

