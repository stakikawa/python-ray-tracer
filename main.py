from color import Color
from color import write_color
from hittable import HitRecord
from hittable_list import HittableList
from ray import Ray
from point3 import Point3
from sphere import Sphere
from vec3 import Vec3
from vec3 import unit_vector
from vec3 import dot
from utility import INFINITY
import math


def ray_color(r, world):
    rec = HitRecord()
    if world.hit(r, 0, INFINITY, rec):
        return 0.5 * (rec.normal + Color(1, 1, 1))
    unit_direction = unit_vector(r.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


def main():
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = math.floor(image_width / aspect_ratio)

    # World
    world = HittableList()
    world.add(Sphere(Point3(0, 0, -1), 0.5))
    world.add(Sphere(Point3(0, -100.5, -1), 100))

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Point3(0, 0, 0)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - Vec3(0, 0, focal_length)

    # Render
    print("P3\n", image_width, ' ', image_height, "\n255\n")

    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            u = float(i) / (image_width - 1)
            v = float(j) / (image_height - 1)
            r = Ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
            pixel_color = ray_color(r)
            write_color(pixel_color)


main()
