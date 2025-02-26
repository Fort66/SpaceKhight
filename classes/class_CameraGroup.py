import pygame as pg
from pygame.sprite import Group
from pygame.image import load
from pygame.display import get_surface
from pygame.math import Vector2
from config.sources.backgrounds.source import GALAXY_SECTORS
from logic.class_LevelsGame import LevelsGame

# import gif_pygame
# from Game.source import *
# from icecream import ic
# from Game.LevelsGame import LG
# from Game.source import backgroundSection

class CameraGroup(Group):
    def __init__(self, game=None):
        super().__init__(self)

        self.game = game
        self.display_surface = get_surface()
        # camera offset
        self.offset = Vector2()
        self.half = (
            self.display_surface.get_size()[0] // 2,
            self.display_surface.get_size()[1] // 2,
        )
        self.camera_rect = pg.Rect(10, 10, 10, 10)
        self.keyboard_speed = None
        self.mouse_speed = None
        self.levels_game = LevelsGame()
        self.set_background()

    def set_background(self) -> None:
        self.source = GALAXY_SECTORS[self.levels_game.current_level]
        self.background_surface = load(self.source).convert_alpha()
        self.background_rect = self.background_surface.get_rect()


    def camera_center(self, target):
        self.offset.x = target.rect.centerx - self.half[0]
        self.offset.y = target.rect.centery - self.half[1]

    def custom_draw(self, player):
        self.camera_center(player)
        # background offset
        # self.display_surface.blit(self.gifBackgtound, self.gifRect)
        self.background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background_surface, self.background_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.center):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image_rotation, offset_position)


        self.game.mini_map.update()
