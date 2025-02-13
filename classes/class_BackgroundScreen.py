import pygame as pg
from pygame.locals import *
from pygame.sprite import Sprite
from pygame.image import load
from pygame.math import Vector2



class BackgroundScreen(Sprite):
    def __init__(self, pos, image, group, screen, game, speed):
        super().__init__(group)
        self.pos = pos
        self.direction = Vector2(pos)
        self.group = group
        self.image = image
        self.screen = screen
        self.game = game
        self.speed = speed
        # self.speed = speed
        # self.long = long
        # self.transformation = transformation
        # self.scrolling = scrolling
        self.__post_init__()

    def __post_init__(self):
        self.scrWidht = self.screen.get_width()
        self.scrHeight = self.screen.get_height()

        self.image_rotation = load(self.image).convert_alpha()
        self.rect = self.image_rotation.get_rect(center=self.pos)

    # def eventKey(self):
    #     keys = pg.key.get_pressed()

    #     if keys[pg.K_RIGHT]:
    #         self.scroll('right')
            
    #     if keys[pg.K_LEFT]:
    #         self.scroll('left')

    
    # def scroll(self, direction):
    #     if direction =='right':
    #         if self.bgRectCenter.x <= - self.scrWidht:
    #             self.bgRectCenter.x = 0
    #         self.bgRectCenter.x -= self.speed
            
    #     if direction =='left':
    #         if self.bgRectCenter.x >= self.scrWidht:
    #             self.bgRectCenter.x = 0
    #         self.bgRectCenter.x += self.speed

    #     self.bgRectLeft.x = self.bgRectCenter.x - (self.bgRectCenter[2] - self.speed)
    #     self.bgRectRight.x = self.bgRectCenter.x + (self.bgRectCenter[2] - self.speed)

    # def blitBG(self):
    #     self.screen.blit(self.bgList[0], self.bgRectLeft)
    #     self.screen.blit(self.bgList[1], self.bgRectCenter)
    #     self.screen.blit(self.bgList[2], self.bgRectRight)
    
    def update(self):
        self.rect.center += self.direction * self.speed