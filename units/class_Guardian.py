from pygame.sprite import Sprite
from classes.class_Animator import Animator


class Guardian(Animator):
    def __init__(
        self,
        dir_path=None,
        speed_frame=0.05,
        obj_rect=None,
        guard_level=None,
        group=None,
    ):
        super().__init__(
            dir_path,
            speed_frame,
            obj_rect,
        )

        self.group = group
        self.guard_level = guard_level

        self.group.add(self)
