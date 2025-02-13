from pygame.sprite import Sprite
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed
import math

from icecream import ic

from config.sources.heroes.source import HEROES
from units.class_Shots import Shots
from units.class_Guardian import Guardian
from config.create_Objects import screen

from logic.class_FirstShot import FirstShot



class Player(Sprite):
    def __init__(
                self,
                pos=(0, 0),
                group=None,
                shot_group=None
                ):
        super().__init__(group)

        self.group = group
        self.pos = pos
        # self.size = size
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = 10
        self.speed = 7
        self.shot_group = shot_group
        self.first_shot = FirstShot()
        self.__post_init__()
        self.group.add(self)


    def __post_init__(self):
        self.image_rotation = HEROES[1]['angle'][0]['sprite']
        self.rect = self.image_rotation.get_rect(center=self.pos)

        self.shield = Guardian(
                                dir_path='images/Guards/guard1',
                                speed_frame=.09,
                                obj_rect=self.rect,
                                angle=self.angle
                                )

        self.prepare_weapon(0)


    def prepare_weapon(self, angle):
        self.pos_weapons = []
        for value in HEROES[1]['angle'][angle]['weapons']:
            self.pos_weapons.append(value)


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
        for value in self.pos_weapons_rotation:
            self.group.add(shot:=
                            Shots(
                                pos=(value),
                                screen=screen,
                                group=self.group,
                                angle=self.angle,
                                speed=10,
                                kill_shot_distance=2000,
                                shoter=self,
                                image='images/Shots/shot3.png',
                                scale_value=.15
                                )
                            )
            self.shot_group.add(shot)


    @property
    def pos_weapons_rotation(self):
        result = []
        for value in self.pos_weapons:
            newX, newY = self.vector_rotation(value, -self.angle / 180 * math.pi)
            result.append([self.rect.centerx + newX, self.rect.centery + newY])
        return result


    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)


    def rotation(self):
        for value in HEROES[1]['angle']:
            if self.angle <= value:
                self.image = HEROES[1]['angle'][value]['sprite']
                self.prepare_weapon(value)
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)

        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def check_position(self):
        if self.rect.left <= self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
        if self.rect.right >= self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
        if self.rect.top <= self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
        if self.rect.bottom >= self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom


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
        self.shield.animate(self.rect, self.angle)

        for value in self.pos_weapons_rotation:
            value[0] += self.direction.x
            value[1] += self.direction.y






