from vec3 import Vec3
from utility import clamp
import math

class Color(Vec3):
    pass


def write_color(pixel_color, samples_per_pixel=1):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide color by number of samples and gamma correct with gamma = 2
    scale = 1.0 / samples_per_pixel
    r = math.sqrt(r * scale)
    g = math.sqrt(g * scale)
    b = math.sqrt(b * scale)

    r = int(256 * clamp(r, 0.0, 0.999))
    g = int(256 * clamp(g, 0.0, 0.999))
    b = int(256 * clamp(b, 0.0, 0.999))
    print(r, ' ', g, ' ', b, '\n')
