from .vec3 import Vec3

class Ray:
    def __init__(self, orig=Vec3(0,0,0), d=Vec3(1,0,0)):
        self.__origin = orig
        self.__direction = d

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    def point_at(self, t):
        return self.__origin + (t * self.__direction)