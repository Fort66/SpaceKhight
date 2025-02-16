import pygame as pg
from pygame.transform import scale_by

from config.create_Objects import screen
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic


class MiniMap:
    def __init__(self):

        self.sprite_groups = SpriteGroups()
        self.old_screen_size = screen.window.get_size()
        self.set_map()

    def change_size_map(self):
        if screen.window.get_size() != self.old_screen_size:
            self.set_map()

    def set_map(self):
        self.map_surface = pg.Surface(screen.window.get_size(), pg.SRCALPHA)
        self.map_surface = scale_by(self.map_surface, 0.25)
        self.map_size = self.map_surface.get_size()
        self.map_surface.fill((0, 100, 0, 50))
        self.ratioX = (
            self.map_size[0] / self.sprite_groups.camera_group.background_rect[2]
        )
        self.ratioY = (
            self.map_size[1] / self.sprite_groups.camera_group.background_rect[3]
        )
        self.map_rect = self.map_surface.get_rect(bottomright=screen.rect.bottomright)

    def draw_player(self):
        for player in self.sprite_groups.player_group:
            pg.draw.circle(
                self.map_surface,
                "yellow",
                (
                    int(player.rect.centerx * self.ratioX),
                    int(player.rect.centery * self.ratioY),
                ),
                2,
            )

    def draw_enemies(self):
        for enemy in self.sprite_groups.enemies_group:
            pg.draw.circle(
                self.map_surface,
                "red",
                (
                    int(enemy.rect.centerx * self.ratioX),
                    int(enemy.rect.centery * self.ratioY),
                ),
                2,
            )

    def draw_player_shot(self):
        for shot in self.sprite_groups.player_shot_group:
            pg.draw.circle(
                self.map_surface,
                "Lime",
                (
                    int(shot.rect.centerx * self.ratioX),
                    int(shot.rect.centery * self.ratioY),
                ),
                1,
            )

    def draw_enemies_shot(self):
        for shot in self.sprite_groups.enemies_shot_group:
            pg.draw.circle(
                self.map_surface,
                "Fuchsia",
                (
                    int(shot.rect.centerx * self.ratioX),
                    int(shot.rect.centery * self.ratioY),
                ),
                1,
            )

    def update(self):
        self.change_size_map()
        self.map_surface.fill((0, 100, 0, 50))
        self.draw_player()
        self.draw_enemies()
        self.draw_player_shot()
        self.draw_enemies_shot()
        screen.window.blit(
            self.map_surface,
            (screen.rect[2] - self.map_size[0], screen.rect[3] - self.map_size[1]),
        )
