from Original.material import Material
from Original.ray import Ray
from Original.vec3 import reflect
from Original.vec3 import unit_vector
from Original.vec3 import random_in_unit_sphere
from Original.vec3 import dot


class Metal(Material):

    def __init__(self, albedo, fuzz=0):
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, r_in, rec):
        reflected = reflect(unit_vector(r_in.direction), rec.normal)
        scattered = Ray(rec.p, reflected + self.fuzz*random_in_unit_sphere())
        attenuation = self.albedo
        return dot(scattered.direction, rec.normal) > 0, attenuation, scattered
