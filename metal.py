from material import Material
from ray import Ray
from vec3 import reflect
from vec3 import unit_vector
from vec3 import dot


class Metal(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, rec):
        reflected = reflect(unit_vector(r_in.direction), rec.normal)
        scattered = Ray(rec.p, reflected)
        attenuation = self.albedo
        return dot(scattered.direction(), rec.normal) > 0, attenuation, scattered
