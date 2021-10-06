from PyTorch.utility import write_color, unit_vector, length, INFINITY
from PyTorch.utility import random_vec, random_vec_mm, random_double
from PyTorch.hittable import HitRecord
from PyTorch.hittable_list import HittableList
from PyTorch.sphere import Sphere
from PyTorch.lambertian import Lambertian
from PyTorch.dielectric import Dielectric
from PyTorch.metal import Metal
from PyTorch.camera import Camera
import math
import torch


def random_scene():
    world = HittableList()

    ground_material = Lambertian(torch.tensor([0.5, 0.5, 0.5]))
    world.add(Sphere(torch.tensor([0, -1000, 0]), 1000, ground_material))

    for a in range(-11, 11):
        for b in range(-11, 11):
            choose_mat = random_double()
            center = torch.tensor([a + 0.9 * random_double(), 0.2, b + 0.9 * random_double()])

            if length(center - torch.tensor([4, 0.2, 0])) > 0.9:

                if choose_mat < 0.8:
                    # diffuse
                    albedo = random_vec() * random_vec()
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    # metal
                    albedo = random_vec_mm(0.5, 1)
                    fuzz = random_double(0, 0.5)
                    sphere_material = Metal(albedo, fuzz)
                    world.add(Sphere(center, 0.2, sphere_material))
                else:
                    # glass
                    sphere_material = Dielectric(1.5)
                    world.add(Sphere(center, 0.2, sphere_material))

    material1 = Dielectric(1.5)
    world.add(Sphere(torch.tensor([0.0, 1.0, 0.0]), 1.0, material1))

    material2 = Lambertian(torch.tensor([0.4, 0.2, 0.1]))
    world.add(Sphere(torch.tensor([-4.0, 1.0, 0.0]), 1.0, material2))

    material3 = Metal(torch.tensor([0.7, 0.6, 0.5]))
    world.add(Sphere(torch.tensor([4.0, 1.0, 0.0]), 1.0, material3))

    return world


def ray_color(r, world, depth):
    cur_ray = r
    cur_attenuation = torch.ones(3)
    for i in range(depth):
        rec = HitRecord()
        if world.hit(cur_ray, 0.001, INFINITY, rec):
            valid, attenuation, scattered = rec.material.scatter(r, rec)
            if valid:
                cur_attenuation *= attenuation
                cur_ray = scattered
            else:
                return torch.zeros(3)
        else:
            unit_direction = unit_vector(cur_ray.direction)
            t = 0.5 * (unit_direction[1] + 1.0)
            c = (1.0 - t) * torch.ones(3) + t * torch.tensor([0.5, 0.7, 1.0])
            return cur_attenuation * c
    return torch.zeros(3)


def main():
    # Image
    aspect_ratio = 3.0 / 2.0
    image_width = 1200
    image_height = math.floor(image_width / aspect_ratio)
    samples_per_pixel = 500
    max_depth = 50

    # World
    world = random_scene()

    # Camera
    lookfrom = torch.tensor([13.0, 2.0, 3.0])
    lookat = torch.tensor([0.0, 0.0, 0.0])
    vup = torch.tensor([0.0, 1.0, 0.0])
    dist_to_focus = 10.0
    aperture = 0.1
    fov = 20.0

    cam = Camera(lookfrom, lookat, vup, fov, aspect_ratio, aperture, dist_to_focus)

    # Render
    num_pixels = image_width * image_height
    pixel_color = torch.zeros(num_pixels, 3)

    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            pixel_index = (j * image_width) + i
            color = torch.zeros(3)
            for s in range(samples_per_pixel):
                u = (i + random_double()) / (image_width - 1)
                v = (j + random_double()) / (image_height - 1)
                r = cam.get_ray(u, v)
                color += ray_color(r, world, max_depth)
            color /= samples_per_pixel
            color = torch.sqrt(color)
            pixel_color[pixel_index] = color

    # Write to File
    print("P3\n", image_width, ' ', image_height, "\n255\n")
    for j in range(image_height - 1, -1, -1):
        for i in range(image_width):
            pixel_index = (j * image_width) + i
            write_color(pixel_color[pixel_index])

# main()
