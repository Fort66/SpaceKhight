from pygame.sprite import (
    groupcollide,
    spritecollide
    )
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic

sprite_groups = SpriteGroups()

def player_collision():
    object_collide = groupcollide(
        sprite_groups.enemies_shot_group,
        sprite_groups.player_group,
        dokilla=True,
        dokillb=False
        )
    # if object_collide:

    #     if obj.guard_level > 0:
    #         obj.guard_level -= 1

    #     if obj.guard_level == 0:
    #         obj.kill()