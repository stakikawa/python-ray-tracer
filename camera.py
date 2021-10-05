from point3 import Point3
from vec3 import Vec3
from vec3 import unit_vector
from vec3 import cross
from ray import Ray
from utility import degrees_to_radians
import math


class Camera:

    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio):
        theta = degrees_to_radians(vfov)
        h = math.tan(theta / 2)
        viewport_height = 2.0 * h
        viewport_width = aspect_ratio * viewport_height

        w = unit_vector(lookfrom - lookat)
        u = unit_vector(cross(vup, w))
        v = cross(w, u)

        self.origin = lookfrom
        self.horizontal = viewport_width * u
        self.vertical = viewport_height * v
        self.lower_left_corner = self.origin - (self.horizontal / 2) - (self.vertical / 2) - w

    def get_ray(self, s, t):
        return Ray(self.origin, self.lower_left_corner + s * self.horizontal + t * self.vertical - self.origin)
