import pygame as pg

pg.mixer.pre_init(44100, -16, 2, 2048)

from icecream import ic

from config.create_Objects import screen

from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from classes.class_BackgroundScreen import BackgroundScreen
from classes.class_SpriteGroups import SpriteGroups

from units.class_Player import Player
from units.class_Enemies import Enemies

from UI.Screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.screen = screen
        self.check_events = CheckEvents(self)
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(game=self)

        self.mini_map = MiniMap(scale_value=0.2, color_map=(0, 100, 0, 170))
        self.dt = 0
        self.setup()

    def setup(self):
        self.player = Player(pos=screen.rect.center)

        for _ in range(5):
            self.sprite_groups.camera_group.add(Enemies(player=self.player))

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.sprite_groups.camera_group.update()

            self.sprite_groups.camera_group.custom_draw(self.player)

            # self.mini_map.update()

            # if pg.sprite.groupcollide(self.player_group, self.enemies_group, False, False):
            #     ic('enemy')
            # if pg.sprite.groupcollide(self.player_group, self.enemy_shot_group, False, False):
            #     ic('emeny shot')
            # if pg.sprite.groupcollide(self.enemies_group, self.player_shot_group, False, False):
            #     ic('player shot')
            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
            # self.dt = self.clock.tick(self.fps)/1000.0
            # self.dt = self.clock.tick(self.fps) / 1000
