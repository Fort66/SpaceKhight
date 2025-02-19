from pygame.math import Vector2
import math


def pos_weapons_rotation(self):
    result = []
    for value in self.pos_weapons:
        newX, newY = vector_rotation(value, -self.angle / 180 * math.pi)
        result.append([self.rect.centerx + newX, self.rect.centery + newY])
    return result

def vector_rotation(vector, angle):
    vector = Vector2(vector)
    return vector.rotate_rad(angle)