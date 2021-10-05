from PyTorch.material import Material
from PyTorch.ray import Ray
from PyTorch.utility import random_unit_vector, near_zero


class Lambertian(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + random_unit_vector()

        # Catch degenerate scatter direction
        if near_zero(scatter_direction):
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)
        attenuation = self.albedo
        return True, attenuation, scattered
