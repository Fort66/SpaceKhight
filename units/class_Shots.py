import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.transform import rotozoom, scale_by
from pygame.image import load

from icecream import ic


class Shots(Sprite):
    def __init__(
                self,
                pos=(0, 0),
                group=None,
                screen=None,
                size=(10, 2),
                color='white',
                speed=0,
                angle=0,
                shoter=None,
                kill_shot_distance=None,
                image=None,
                scale_value=None,
                damage=None
                ):
        super().__init__(group)

        self.screen = screen
        self.group = group
        self.angle = angle
        self.shoter = shoter
        self.damage = damage
        self.kill_shot_distance = kill_shot_distance
        self.old_shot_coordinate = Vector2(self.shoter.rect.center)
        if image:
            self.image = scale_by(load(image).convert_alpha(), scale_value)
        else:
            self.image = pg.Surface(size, pg.SRCALPHA)
            self.image.fill(color)

        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=pos)
        # self.vector = Vector2(self.rect.center)
        self.offset = Vector2().rotate(self.angle)
        self.pos = Vector2(pos) + self.offset
        self.direction = Vector2(1, 0).rotate(-self.angle)
        self.speed = speed
        self.shield = None
        # self.group.add(self)
        # self


    def check_position(self):
        if Vector2(self.rect.center).distance_to(self.old_shot_coordinate) > self.kill_shot_distance:
            self.kill()

    def move(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos
        # self.rect.move_ip(self.speed, self.speed)
        # self.rect.center = self.pos


    def update(self):
        self.check_position()
        self.move()