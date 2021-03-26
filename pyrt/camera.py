from pyrt.vec3 import Vec3
from pyrt.point import Point3
from pyrt.ray import Ray

class Camera:
    def __init__(self, width, height):
        ascpect_ratio = width / height

        viewport_height = 2.0   
        viewport_width = ascpect_ratio * viewport_height

        focal_length = 1.0

        self.__origin = Point3(0,0,0)
        self.__horizontal = Vec3(viewport_width, 0, 0)
        self.__vertical = Vec3(0, viewport_height, 0)

        self.__lower_left_corner = self.__origin - self.__horizontal/2 - self.__vertical/2 - Vec3(0,0,focal_length)

    def ray(self, u, v):
        d = self.__lower_left_corner + u*self.__horizontal + v*self.__vertical - self.__origin
        return Ray(self.__origin, d.normalize())