from Original.vec3 import unit_vector
from Original.vec3 import cross
from Original.vec3 import random_in_unit_disk
from Original.ray import Ray
from Original.utility import degrees_to_radians
import math


class Camera:

    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio, aperture, focus_dist):
        theta = degrees_to_radians(vfov)
        h = math.tan(theta / 2)
        viewport_height = 2.0 * h
        viewport_width = aspect_ratio * viewport_height

        self.w = unit_vector(lookfrom - lookat)
        self.u = unit_vector(cross(vup, self.w))
        self.v = cross(self.w, self.u)

        self.origin = lookfrom
        self.horizontal = focus_dist * viewport_width * self.u
        self.vertical = focus_dist * viewport_height * self.v
        self.lower_left_corner = self.origin - (self.horizontal / 2) - (self.vertical / 2) - (focus_dist * self.w)
        self.lens_radius = aperture / 2

    def get_ray(self, s, t):
        rd = self.lens_radius * random_in_unit_disk()
        offset = self.u * rd.x() + self.v * rd.y()

        return Ray(self.origin + offset,
                   self.lower_left_corner + (s * self.horizontal) + (t * self.vertical) - self.origin - offset)
