import math

class Vec3:

    def __init__(self, x=0, y=0, z=0):
        self.e = [x, y, z]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __add__(self, other):
        if isinstance(other, type(self)):
            x = self.e[0] + other.e[0]
            y = self.e[1] + other.e[1]
            z = self.e[2] + other.e[2]
            return Vec3(x, y, z)
        else:
            x = self.e[0] + other
            y = self.e[1] + other
            z = self.e[2] + other
            return Vec3(x, y, z)

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.e[0] += other.e[0]
            self.e[1] += other.e[1]
            self.e[2] += other.e[2]
            return self
        else:
            self.e[0] += other
            self.e[1] += other
            self.e[2] += other
            return self

    def __sub__(self, other):
        if isinstance(other, type(self)):
            x = self.e[0] - other.e[0]
            y = self.e[1] - other.e[1]
            z = self.e[2] - other.e[2]
            return Vec3(x, y, z)
        else:
            x = self.e[0] - other
            y = self.e[1] - other
            z = self.e[2] - other
            return Vec3(x, y, z)

    def __isub__(self, other):
        if isinstance(other, type(self)):
            self.e[0] -= other.e[0]
            self.e[1] -= other.e[1]
            self.e[2] -= other.e[2]
            return self
        else:
            self.e[0] -= other
            self.e[1] -= other
            self.e[2] -= other
            return self

    def __mul__(self, other):
        if isinstance(other, type(self)):
            x = self.e[0] * other.e[0]
            y = self.e[1] * other.e[1]
            z = self.e[2] * other.e[2]
            return Vec3(x, y, z)
        else:
            x = self.e[0] * other
            y = self.e[1] * other
            z = self.e[2] * other
            return Vec3(x, y, z)

    def __imul__(self, other):
        if isinstance(other, type(self)):
            self.e[0] *= other.e[0]
            self.e[1] *= other.e[1]
            self.e[2] *= other.e[2]
            return self
        else:
            self.e[0] *= other
            self.e[1] *= other
            self.e[2] *= other
            return self

    def __truediv__(self, other):
        t = 1 / other
        x = self.e[0] * t
        y = self.e[1] * t
        z = self.e[2] * t
        return Vec3(x, y, z)

    def __itruediv__(self, other):
        t = 1 / other
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __getitem__(self, key):
        return self.e[key]

    def __neg__(self):
        x = -self.e[0]
        y = -self.e[1]
        z = -self.e[2]
        return Vec3(x, y, z)

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def length(self):
        return math.sqrt(self.length_squared())

def unit_vector(v):
    return v / v.length()

def dot(a, b):
    return a.e[0] * b.e[0] + a.e[1] * b.e[1] + a.e[2] * b.e[2]

def cross(a, b):
    return Vec3(a.e[1] * b.e[2] - a.e[2] * b.e[1],
                a.e[2] * b.e[0] - a.e[0] * b.e[2],
                a.e[0] * b.e[1] - a.e[1] * b.e[0])
