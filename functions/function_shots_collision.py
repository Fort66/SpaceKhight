from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic


def shots_collision(obj):
    sprite_groups = SpriteGroups()

    # ehits = spritecollide(obj, sprite_groups.enemies_group, dokill=False, collided=None)

    # phits = spritecollide(obj, sprite_groups.player_group, dokill=False, collided=None)
    # if phits:
    #     old_rect = phits[0].rect
    #     expl_enemies_rocket = Explosion(
    #             dir_path='images/explosions/rocket1_expl',
    #             speed_frame=.09,
    #             obj_rect=None,
    #             scale_value=(1, 1),
    #             loops=1,
    #             pos=old_rect.center
    #         )

    objects_collide = groupcollide(
        sprite_groups.enemies_shot_group,
        sprite_groups.player_group,
        dokilla=False,
        dokillb=False,
        collided=None,
    )
    if objects_collide:
        hits_key = list(objects_collide.keys())[0]
        hits_value = list(objects_collide.values())[0][0]
        hits_value.rocket_position = hits_key.rect.center
        hits_value.explosion = Explosion(
            dir_path="images/explosions/rocket1_expl",
            speed_frame=0.09,
            obj_rect=None,
            scale_value=(1, 1),
            loops=1,
            pos=hits_value.rocket_position,
        )
