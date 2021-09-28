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
from vec3 import random_in_unit_sphere
from vec3 import random_unit_vector
from lambertian import Lambertian
from metal import Metal
from camera import Camera
from utility import INFINITY
from utility import random_double
import math


def ray_color(r, world, depth):
    rec = HitRecord()
    if depth <= 0:
        return Color(0, 0, 0)
    if world.hit(r, 0.001, INFINITY, rec):
        valid, scattered, attenuation = rec.material.scatter(r, rec)
        if valid:
            return attenuation * ray_color(scattered, world, depth - 1)
        return Color(0, 0, 0)
    unit_direction = unit_vector(r.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)


def main():
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = math.floor(image_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 50

    # World
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.7, 0.3, 0.3))
    material_left = Metal(Color(0.8, 0.8, 0.8), 0.3)
    material_right = Metal(Color(0.8, 0.6, 0.2), 1.0)

    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right))

    # Camera
    cam = Camera()

    # Render
    anti_alias = True
    print("P3\n", image_width, ' ', image_height, "\n255\n")

    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            pixel_color = Color(0, 0, 0)
            if anti_alias:
                for s in range(samples_per_pixel):
                    u = float(i + random_double()) / (image_width - 1)
                    v = float(j + random_double()) / (image_height - 1)
                    r = cam.get_ray(u, v)
                    pixel_color += ray_color(r, world, max_depth)
                write_color(pixel_color, samples_per_pixel)
            else:
                u = float(i) / (image_width - 1)
                v = float(j) / (image_height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)
                write_color(pixel_color)


main()
