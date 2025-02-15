import pygame as pg
from pygame.display import get_surface
from pygame.image import load
from pygame.sprite import Group
from pygame.math import Vector2

# from Game.LevelsGame import LG
# from Game.source import backgroundSection

back = 'images/tmp/back6.jpg'

class CameraGroup(Group):
    def __init__(
                self,
                game = None
                ):
        super().__init__(self)

        self.game = game
        self.display_surface = get_surface()
        self.offset = Vector2()
        self.__post_init__()
        # self.keyboard_speed = None
        # self.mouse_speed = None


    def __post_init__(self):
        self.half = (
                    self.display_surface.get_size()[0] // 2,
                    self.display_surface.get_size()[1] // 2
                    )
        self.camera_rect = pg.Rect(10, 10, 10, 10)
        self.set_background()


    def set_background(self):
        self.source = back
        # self.gifBackgtound = gif_pygame.load('Images/Back/gif/2.gif')
        # self.gifRect = self.gifBackgtound.get_rect()
        self.background_surface = load(self.source).convert_alpha()
        # self.backgroundRect = self.backgroundSurface.get_rect(center = self.half)
        self.background_rect = self.background_surface.get_rect()
        # ic(self.backgroundRect)


    def camera_center(
                    self,
                    target
                    ):
        self.offset.x = target.rect.centerx - self.half[0]
        self.offset.y = target.rect.centery - self.half[1]


    def custom_draw(
                    self,
                    player
                    ):
        self.camera_center(player)
        self.background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background_surface, self.background_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.center):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image_rotation, offset_position)

            if hasattr(sprite, 'shield') and sprite.shield:
                self.display_surface.blit(sprite.shield.frames[sprite.shield.frame][0], offset_position)
        
        self.game.mini_map.update()
