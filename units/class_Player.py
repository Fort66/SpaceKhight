from pygame.sprite import Sprite, spritecollideany, spritecollide
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

import math

from config.sources.heroes.source import HEROES
from config.create_Objects import screen, checks, weapons

from units.class_Shots import Shots
from units.class_Guardian import Guardian

from classes.class_SpriteGroups import SpriteGroups

from functions.function_player_collision import guard_collision
from functions.function_weapons import pos_weapons_rotation, vector_rotation


class Player(Sprite):
    def __init__(
        self,
        pos=(0, 0),
    ):

        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.camera_group.add(self)
        self.sprite_groups.player_group.add(self)
        # self.sprite_groups.all_sprites_group.add(self)

        self.pos = pos
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = 10
        self.speed = 7


        self.first_shot = False

        self.__post_init__()

    def __post_init__(self):
        self.image = HEROES[1]["angle"][0]["sprite"]
        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect(center=self.pos)

        self.shield = Guardian(
            dir_path="images/Guards/guard1",
            speed_frame=0.09,
            obj_rect=self.rect,
            scale_value=(1, 1),
            loops=-1,
            guard_level=10,
            pos=self.rect.center
            # cover=True
        )

        self.prepare_weapon(0)

    def prepare_weapon(self, angle):
        weapons.load_weapons(self, HEROES[1]["angle"][angle]["weapons"], angle)

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(self, self.angle)

    def rotation(self):
        for value in HEROES[1]["angle"]:
            if self.angle <= value:
                self.image = HEROES[1]["angle"][value]["sprite"]
                self.prepare_weapon(value)
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == -1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()

            elif event.y == 1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.first_shot:
                    self.first_shot = not self.first_shot
                self.shot()

    def shot(self):
        value = self.pos_weapons_rotation()
        for pos in value:
            self.sprite_groups.camera_group.add(
                shot := Shots(
                    pos=(pos),
                    screen=screen,
                    angle=self.angle,
                    speed=10,
                    kill_shot_distance=2000,
                    shoter=self,
                    image="images/Shots/shot3.png",
                    scale_value=0.15,
                )
            )
            self.sprite_groups.player_shot_group.add(shot)

    def check_position(self):
        checks.position(self, self.sprite_groups.camera_group.background_rect)

    def move(self):
        keys = get_pressed()
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)

    def update(self):
        self.check_position()
        self.move()
        if hasattr(self, "shield"):
            self.shield.animate(self.rect)
            guard_collision(self)

        # self.check_collision(self)
        
        if hasattr(self, 'explosion'):
            self.explosion.animate(self.rect)



        value = self.pos_weapons_rotation()
        for pos in value:
            pos[0] += self.direction.x
            pos[1] += self.direction.y
        # value[0] += self.direction.x
        # value[1] += self.direction.y
