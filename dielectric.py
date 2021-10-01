from material import Material
from color import Color
from vec3 import unit_vector
from vec3 import refract
from vec3 import reflect
from vec3 import Vec3
from vec3 import dot
from ray import Ray
import math


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

        if cannot_refract:
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio)

        scattered = Ray(rec.p, direction)
        return True, attenuation, scattered
