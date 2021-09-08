from point3 import Point3
from vec3 import Vec3
from dataclasses import dataclass


@dataclass
class HitRecord:
    p: Point3
    normal: Vec3
    t: float


class Hittable:
    def hit(self, r, t_min, t_max, rec):
        raise NotImplementedError()
