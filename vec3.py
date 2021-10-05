import math
from utility import random_double


class Vec3:

    def __init__(self, x=0, y=0, z=0):
        self.e = [x, y, z]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __add__(self, other):
        if isinstance(other, Vec3):
            x = self.e[0] + other.e[0]
            y = self.e[1] + other.e[1]
            z = self.e[2] + other.e[2]
            return Vec3(x, y, z)
        else:
            x = self.e[0] + other
            y = self.e[1] + other
            z = self.e[2] + other
            return Vec3(x, y, z)

    def __iadd__(self, other):
        if isinstance(other, Vec3):
            self.e[0] += other.e[0]
            self.e[1] += other.e[1]
            self.e[2] += other.e[2]
            return self
        else:
            self.e[0] += other
            self.e[1] += other
            self.e[2] += other
            return self

    def __sub__(self, other):
        if isinstance(other, Vec3):
            x = self.e[0] - other.e[0]
            y = self.e[1] - other.e[1]
            z = self.e[2] - other.e[2]
            return Vec3(x, y, z)
        else:
            x = self.e[0] - other
            y = self.e[1] - other
            z = self.e[2] - other
            return Vec3(x, y, z)

    def __isub__(self, other):
        if isinstance(other, Vec3):
            self.e[0] -= other.e[0]
            self.e[1] -= other.e[1]
            self.e[2] -= other.e[2]
            return self
        else:
            self.e[0] -= other
            self.e[1] -= other
            self.e[2] -= other
            return self

    def __mul__(self, other):
        if isinstance(other, Vec3):
            x = self.e[0] * other.e[0]
            y = self.e[1] * other.e[1]
            z = self.e[2] * other.e[2]
            return Vec3(x, y, z)
        else:
            x = self.e[0] * other
            y = self.e[1] * other
            z = self.e[2] * other
            return Vec3(x, y, z)

    def __imul__(self, other):
        if isinstance(other, Vec3):
            self.e[0] *= other.e[0]
            self.e[1] *= other.e[1]
            self.e[2] *= other.e[2]
            return self
        else:
            self.e[0] *= other
            self.e[1] *= other
            self.e[2] *= other
            return self

    __radd__ = __add__
    __rmul__ = __mul__

    def __truediv__(self, other):
        t = 1 / other
        x = self.e[0] * t
        y = self.e[1] * t
        z = self.e[2] * t
        return Vec3(x, y, z)

    def __itruediv__(self, other):
        t = 1 / other
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __getitem__(self, key):
        return self.e[key]

    def __neg__(self):
        x = -self.e[0]
        y = -self.e[1]
        z = -self.e[2]
        return Vec3(x, y, z)

    def near_zero(self):
        s = 1e-8
        return (abs(self.e[0]) < s) and (abs(self.e[1]) < s) and (abs(self.e[2]) < s)

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def length(self):
        return math.sqrt(self.length_squared())


def random_vec():
    return Vec3(random_double(), random_double(), random_double())


def random_vec_mm(min, max):
    return Vec3(random_double(min, max), random_double(min, max), random_double(min, max))


def random_in_unit_sphere():
    while True:
        p = random_vec_mm(-1, 1)
        if p.length_squared() >= 1:
            continue
        return p


def random_in_unit_disk():
    while True:
        p = Vec3(random_double(-1, 1), random_double(-1, 1), 0)
        if p.length_squared() >= 1:
            continue
        return p


def random_unit_vector():
    return unit_vector(random_in_unit_sphere())


def unit_vector(v):
    return v / v.length()


def reflect(v, n):
    return v - 2 * dot(v, n) * n


def refract(uv, n, etai_over_etat):
    cos_theta = min(dot(-uv, n), 1.0)
    r_out_perp = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel = -math.sqrt(abs(1.0 - r_out_perp.length_squared())) * n
    return r_out_perp + r_out_parallel


def dot(a, b):
    return a.e[0] * b.e[0] + a.e[1] * b.e[1] + a.e[2] * b.e[2]


def cross(a, b):
    return Vec3(a.e[1] * b.e[2] - a.e[2] * b.e[1],
                a.e[2] * b.e[0] - a.e[0] * b.e[2],
                a.e[0] * b.e[1] - a.e[1] * b.e[0])
