class Intersection:
    def __init__(self, point, normal, t, material):
        self.__point = point
        self.__normal = normal
        self.__t = t
        self.__material = material

    @property
    def point(self):
        return self.__point

    @property
    def normal(self):
        return self.__normal

    @property
    def t(self):
        return self.__t

    @property
    def material(self):
        return self.__material