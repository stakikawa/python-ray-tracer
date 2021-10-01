from material import Material
from color import Color
from vec3 import unit_vector
from vec3 import refract
from vec3 import reflect
from vec3 import random_double
from vec3 import dot
from ray import Ray
import math


def reflectance(cosine, ref_idx):
    # Use Schlick's Approximation
    r0 = (1 - ref_idx) / (1 + ref_idx)
    r0 = r0 * r0
    return r0 + (1 - r0) * pow((1 - cosine), 5)


class Dielectric(Material):

    def __init__(self, index_of_refraction):
        self.ir = index_of_refraction

    def scatter(self, r_in, rec):
        attenuation = Color(1.0, 1.0, 1.0)
        refraction_ratio = (1.0 / self.ir) if rec.front_face else self.ir

        unit_direction = unit_vector(r_in.direction)

        cos_theta = min(dot(-unit_direction, rec.normal), 1.0)
        sin_theta = math.sqrt(1.0 - cos_theta * cos_theta)

        cannot_refract = refraction_ratio * sin_theta > 1.0

        if cannot_refract or reflectance(cos_theta, refraction_ratio) > random_double():
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio)

        scattered = Ray(rec.p, direction)
        return True, attenuation, scattered
