import pygame as pg
# import gif_pygame as gif


from icecream import ic

# Инициализация звука. Инициализация плейера. (частота, биты (Если значение отрицательное, то будут использоваться подписанные значения выборки. Положительные значения означают, что будут использоваться неподписанные аудиосэмплированные выборки. Неверное значение вызывает исключение), каналы, буфер)
pg.mixer.pre_init(44100, -16, 2, 2048)

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemies
from classes.class_BackgroundScreen import BackgroundScreen




class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.screen = screen
        self.win_width = screen.window.get_width()
        self.win_height = screen.window.get_height()
        self.check_events = CheckEvents(self)
        self.create_groups()
        self.setup()

    def setup(self):
        self.player = Player(
                            pos=screen.rect.center,
                            group=self.camera_group,
                            shot_group=self.player_shot_group,
                            )
        self.player_group.add(self.player)

        for _ in range(10):
            self.camera_group.add(
                                Enemies(
                                        group=self.camera_group,
                                        player=self.player,
                                        shot_group=self.enemy_shot_group,
                                        )
                                )
            self.enemies_group.add(self.camera_group.sprites()[1:])

    def create_groups(self):
        self.camera_group = CameraGroup(self)
        self.player_group = pg.sprite.Group()
        self.enemies_group = pg.sprite.Group()
        self.enemy_shot_group = pg.sprite.Group()
        self.player_shot_group = pg.sprite.Group()


    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.camera_group.update()

            self.camera_group.custom_draw(self.player)

            # if pg.sprite.groupcollide(self.player_group, self.enemies_group, False, False):
            #     ic('enemy')
            # if pg.sprite.groupcollide(self.player_group, self.enemy_shot_group, False, False):
            #     ic('emeny shot')
            # if pg.sprite.groupcollide(self.enemies_group, self.player_shot_group, False, False):
            #     ic('player shot')
            # self.screen.update_caption(f'{str(round(self.clock.get_fps(), 2))}')
            # pg.display.update()
            self.clock.tick(self.fps)