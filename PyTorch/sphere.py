from PyTorch.hittable import Hittable
from PyTorch.utility import dot, length_squared
from math import sqrt


class Sphere(Hittable):

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, r, t_min, t_max, rec):
        oc = r.origin - self.center
        a = length_squared(r.direction)
        half_b = dot(oc, r.direction)
        c = length_squared(oc) - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False
        sqrt_d = sqrt(discriminant)

        # Find the nearest root that lies in acceptable t range
        root = (-half_b - sqrt_d) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrt_d) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.material = self.material

        return True
