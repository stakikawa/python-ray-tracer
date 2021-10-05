from Original.hittable import Hittable
from Original.hittable import HitRecord


class HittableList(Hittable):

    def __init__(self, object=None):
        if object is None:
            self.objects = []
        else:
            self.objects = [object]

    def add(self, object):
        self.objects.append(object)

    def clear(self):
        self.objects = []

    def hit(self, r, t_min, t_max, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for object in self.objects:
            if object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.copy(temp_rec)

        return hit_anything
