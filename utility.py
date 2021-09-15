import math
import random

PI = 3.1415926535897932385
INFINITY = math.inf


def degrees_to_radians(degrees):
    return degrees * PI / 180.0


def random_double(min=None, max=None):
    # Returns a random real in [0, 1) or in [min, max)
    if min is None or max is None:
        return random.random()
    else:
        return min + (max - min) * random.random()


def clamp(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
