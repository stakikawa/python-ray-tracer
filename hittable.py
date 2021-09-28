from vec3 import dot


class HitRecord:

    def __init__(self, p=None, normal=None, material=None, t=None):
        self.p = p
        self.normal = normal
        self.material = material
        self.t = t
        self.front_face = False

    def copy(self, rec):
        self.p = rec.p
        self.normal = rec.normal
        self.material = rec.material
        self.t = rec.t
        self.front_face = rec.front_face

    def set_face_normal(self, r, outward_normal):
        self.front_face = dot(r.direction, outward_normal)
        self.normal = outward_normal if self.front_face else -outward_normal


class Hittable:
    def hit(self, r, t_min, t_max, rec):
        raise NotImplementedError()
