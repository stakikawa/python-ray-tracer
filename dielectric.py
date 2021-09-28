from material import Material
from color import Color
from vec3 import unit_vector
from vec3 import refract
from ray import Ray


class Dielectric(Material):

    def __init__(self, index_of_refraction):
        self.ir = index_of_refraction

    def scatter(self, r_in, rec):
        attenuation = Color(1.0, 1.0, 1.0)
        refraction_ratio = (1.0 / self.ir) if rec.front_face else self.ir

        unit_direction = unit_vector(r_in.direction)
        refracted = refract(unit_direction, rec.normal, refraction_ratio)

        scattered = Ray(rec.p, refracted)

        return True, attenuation, scattered
