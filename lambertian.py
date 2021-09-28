from material import Material
from ray import Ray
from vec3 import random_unit_vector


class Lambertian(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + random_unit_vector()
        scattered = Ray(rec.p, scatter_direction)
        attenuation = self.albedo
        return True, attenuation, scattered
