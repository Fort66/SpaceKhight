from pygame.sprite import Sprite
from classes.class_Animator import Animator

from icecream import ic

class Explosion(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        scale_value=None,
        loops=None,
        size=None
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            scale_value=scale_value,
            loops=loops,
            size=size,
        )

        self.obj = obj

    def update(self):
        self.rect.center = self.obj.rect.center
        if self.loops > 0:
            self.image_rotation = self.frames[self.frame][0]
            super().animate()
        else:
            self.kill()
