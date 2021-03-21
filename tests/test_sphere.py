from pyrt.transform import Translation
from pyrt.point import Point3
from pyrt.vec3 import Vec3
from pyrt.ray import Ray
from pyrt.sphere import Sphere
from pyrt.material import Lambert, Metal


def test_ray_intersection():
    s = Sphere(1, Translation(0, 0, 0), Lambert(Vec3(0, 0, 0)))
    ray = Ray(Point3(0, 0, 3), Vec3(0, 0, -1))
    i = s.hit(ray)
    assert i is not None
    assert i.t == 2
    assert i.point == Point3(0, 0, 1)
    assert i.normal == Vec3(0, 0, 1)
    assert isinstance(i.material, Lambert)


def test_ray_intersection_metal_scatter():
    s = Sphere(1, Translation(0, 0, 0), Metal(Vec3(0, 0, 0)))
    ray = Ray(Point3(0, 0, 3), Vec3(0, 0, -1))
    i = s.hit(ray)
    assert i is not None
    assert i.t == 2
    assert i.point == Point3(0, 0, 1)
    assert i.normal == Vec3(0, 0, 1)
    assert isinstance(i.material, Metal)
    reflected = i.material.scatter(ray, i)
    assert reflected is not None
    r, a = reflected
    assert r.direction == Vec3(0, 0, 1)


def test_ray_intersection_miss():
    s = Sphere(1, Translation(0, 0, 0), None)
    ray = Ray(Point3(0, 0, 3), Vec3(0, 1, 0))
    assert s.hit(ray) is None


def test_ray_intersection_min():
    scene = [Sphere(1, Translation(
        0, 0, -5), Lambert(Vec3(0, 0, 0)))]
    ray = Ray(Point3(0, 0, 0), Vec3(0, 0, -1))

    hits = list(map(lambda s: s.hit(ray), scene))
    min_hit = min(hits, key=lambda h: h.t)

    assert min_hit is not None


def test_ray_intersection_no_min():
    scene = [Sphere(1, Translation(0, 0, 5), Lambert(Vec3(0, 0, 0)))]
    ray = Ray(Point3(0, 0, 0), Vec3(0, 0, -1))

    hits = list(filter(None, map(lambda s: s.hit(ray), scene)))
    assert len(hits) == 0
