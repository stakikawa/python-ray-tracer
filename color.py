from vec3 import Vec3

class Color(Vec3):

    @staticmethod
    def write_color(pixel_color):
        ir = int(255.999 * pixel_color.x())
        ig = int(255.999 * pixel_color.y())
        ib = int(255.999 * pixel_color.z())
        print(ir, ' ', ig, ' ', ib, '\n')
