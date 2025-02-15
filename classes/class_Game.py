import pygame as pg
pg.mixer.pre_init(44100, -16, 2, 2048)
from pygame.sprite import Group, GroupSingle

from icecream import ic

from config.create_Objects import screen

from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from classes.class_BackgroundScreen import BackgroundScreen

from units.class_Player import Player
from units.class_Enemies import Enemies

from UI.Screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.screen = screen
        # self.win_width = screen.window.get_width()
        # self.win_height = screen.window.get_height()
        self.check_events = CheckEvents(self)
        self.create_groups()
        self.mini_map = MiniMap(
                                group_list=[
                                            self.camera_group,
                                            self.player_group,
                                            self.enemies_group,
                                            self.player_shot_group,
                                            self.enemy_shot_group,
                                            ]
                                )
        self.dt = 0
        self.setup()


    def setup(self):
        self.player = Player(
                            pos=screen.rect.center,
                            group_list=[
                                        self.camera_group,
                                        self.player_group,
                                        self.player_shot_group,
                                        ]
                            )

        for _ in range(10):
            self.camera_group.add(
                                Enemies(
                                        group_list=[
                                                    self.camera_group,
                                                    self.enemies_group,
                                                    self.enemy_shot_group
                                                    ],
                                        player=self.player,
                                        )
                                )


    def create_groups(self):
        self.camera_group = CameraGroup(self)
        self.player_group = GroupSingle()
        self.enemies_group = Group()
        self.enemy_shot_group = Group()
        self.player_shot_group = Group()


    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.camera_group.update()

            self.camera_group.custom_draw(self.player)

            # self.mini_map.update()

            # if pg.sprite.groupcollide(self.player_group, self.enemies_group, False, False):
            #     ic('enemy')
            # if pg.sprite.groupcollide(self.player_group, self.enemy_shot_group, False, False):
            #     ic('emeny shot')
            # if pg.sprite.groupcollide(self.enemies_group, self.player_shot_group, False, False):
            #     ic('player shot')
            self.screen.update_caption(f'{str(round(self.clock.get_fps(), 2))}')
            pg.display.update()
            self.clock.tick(self.fps)
            # self.dt = self.clock.tick(self.fps)/1000.0
            # self.dt = self.clock.tick(self.fps) / 1000
