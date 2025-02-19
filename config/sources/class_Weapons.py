from pygame.math import Vector2
import math


class Weapons:
    def load_weapons(self, obj, source, angle):
        obj.pos_weapons = []
        for value in source:
            obj.pos_weapons.append(value)

    def pos_rotation(self, obj, angle):
        result = []
        for value in obj.pos_weapons:
            newX, newY = self.vector_rotation(value, -angle / 180 * math.pi)
            result.append([obj.rect.centerx + newX, obj.rect.centery + newY])
        return result

    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)
