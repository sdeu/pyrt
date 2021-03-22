from vec3 import Vec3
from point import Point3
from ray import Ray

class Camera:
    def __init__(self, width):
        ascpect_ratio = 16.0 / 9.0

        viewport_height = 2.0   
        viewport_width = ascpect_ratio * viewport_height

        focal_length = 1.0

        self.__origin = Point3(0,0,0)
        self.__horizontal = Vec3(viewport_width, 0, 0)
        self.__vertical = Vec3(0, viewport_height, 0)

        self.__lower_left_corner = self.__origin - self.__horizontal/2 - self.__vertical/2 - Vec3(0,0,focal_length)

    def ray(self, u, v):
        return Ray(self.__origin, self.__lower_left_corner + u*self.__horizontal + v*self.__vertical - self.__origin)