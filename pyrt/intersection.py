class Intersection:
    def __init__(self, point, normal, t):
        self.__point = point
        self.__normal = normal
        self.__t = t

    @property
    def point(self):
        return self.__point

    @property
    def normal(self):
        return self.__normal

    @property
    def t(self):
        return self.__t