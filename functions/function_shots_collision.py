from pygame.sprite import (
    groupcollide,
    spritecollide
    )
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic

sprite_groups = SpriteGroups()

def player_guard_collision():
    object_collide = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_shot_group,
        dokilla=False,
        dokillb=False
        ) or groupcollide(
            sprite_groups.player_group,
            sprite_groups.enemies_shot_group,
            dokilla=False,
            dokillb=False
            )
    if object_collide:
        hits = list(object_collide.values())[0]
        explosion = Explosion(
            dir_path='images/explosions/rocket1_expl',
            speed_frame=0.02,
            scale_value=(.5, .5),
            loops=1,
            obj=hits[0]

        )



# def enemies_shot_collision(obj):
#     object_collide = groupcollide(sprite_groups.player_shot_group, sprite_groups.enemies_guard_group, dokilla=True, dokillb=False)
#     if object_collide:
#         lot_hits = len(list(object_collide.values()))
#         hits = list(object_collide.values())[0][0]
#         if hits.guard_level > 0:
#             hits.guard_level -= lot_hits

#         if hits.guard_level <= 0:
#             hits.kill()