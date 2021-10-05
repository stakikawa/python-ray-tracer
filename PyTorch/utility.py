import torch
from math import sqrt, inf
import random

PI = 3.1415926535897932385
INFINITY = inf


def degrees_to_radians(degrees):
    return degrees * PI / 180.0


def random_double(min=None, max=None):
    # Returns a random real in [0, 1) or in [min, max)
    if min is None or max is None:
        return random.random()
    else:
        return min + (max - min) * random.random()


def clamp(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x


def random_vec():
    return torch.tensor([random_double(), random_double(), random_double()])


def random_vec_mm(min, max):
    return torch.tensor([random_double(min, max), random_double(min, max), random_double(min, max)])


def random_in_unit_sphere():
    while True:
        p = random_vec_mm(-1, 1)
        if dot(p, p) >= 1:
            continue
        return p


def random_in_unit_disk():
    while True:
        p = torch.tensor([random_double(-1, 1), random_double(-1, 1), 0])
        if dot(p, p) >= 1:
            continue
        return p


def random_unit_vector():
    return unit_vector(random_in_unit_sphere())


def unit_vector(v):
    return v / torch.norm(v)


def reflect(v, n):
    return v - 2 * dot(v, n) * n


def refract(uv, n, etai_over_etat):
    cos_theta = min(dot(-uv, n), 1.0)
    r_out_perp = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel = -sqrt(abs(1.0 - dot(r_out_perp, r_out_perp))) * n
    return r_out_perp + r_out_parallel


def dot(a, b):
    return torch.dot(a, b)


def cross(a, b):
    return torch.cross(a, b)


def near_zero(v):
    s = 1e-8
    return (abs(v[0]) < s) and (abs(v[1]) < s) and (abs(v[2]) < s)


def length_squared(v):
    return dot(v, v)


def length(v):
    return torch.norm(v)
