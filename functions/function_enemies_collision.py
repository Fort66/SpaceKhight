from pygame.sprite import groupcollide
from config.create_Objects import screen

from icecream import ic

from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

sprite_groups = SpriteGroups()

def enemies_collision():
    object_collide = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        dokilla=False,
        dokillb=True
        )
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits = list(object_collide.keys())[0]

        if hits.hp > 0:
            hits.decrease_hp(lot_hits)

        if hits.hp <= 0:
            explosion = Explosion(
                dir_path='images/explosions/es1',
                speed_frame=.12,
                scale_value=(.75, .75),
                loops=1,
                obj=hits,
                angle=hits.angle
            )
            if not explosion:
                hits.kill()