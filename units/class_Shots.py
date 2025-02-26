import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.transform import rotozoom, scale_by
from pygame.image import load

from icecream import ic

from classes.class_SpriteGroups import SpriteGroups
from functions.function_shots_collision import (
    player_guard_collision,
    enemies_guard_collision,
    shots_collision,
    distance_collision
    )

class Shots(Sprite):
    def __init__(
                self,
                pos=(0, 0),
                size=(20, 3),
                color='white',
                speed=0,
                angle=0,
                shoter=None,
                kill_shot_distance=None,
                scale_value=None,
                image=None,
                damage=None,
                owner=None
                ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)

        self.damage = damage
        self.shoter = shoter
        self.kill_shot_distance = kill_shot_distance
        self.angle = angle
        self.speed = speed
        self.size = size
        self.owner = owner
        self.old_shot_coordinate = Vector2(self.shoter.rect.center)
        if image:
            self.image = scale_by(load(image).convert_alpha(), scale_value)
        else:
            self.image = pg.Surface(self.size, pg.SRCALPHA)
            self.image.fill(color)
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=pos)
        self.offset =  Vector2().rotate(self.angle)
        self.pos = Vector2(pos) + self.offset
        self.direction = Vector2(1, 0).rotate(-self.angle)


    def check_position(self):
        if Vector2(self.rect.center).distance_to(self.old_shot_coordinate) > self.kill_shot_distance:
            distance_collision(self)
            self.kill()

    def move(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos


    def update(self):
        self.check_position()
        self.move()
        player_guard_collision(self)
        enemies_guard_collision(self)
        shots_collision()