from classes.class_Animator import Animator

from icecream import ic

class Explosion(Animator):
    def __init__(
        self,
        dir_path,
        speed_frame,
        obj_rect,
        scale_value,
        loops,
        pos
        # cover=False
    ):
        super().__init__(
            dir_path,
            speed_frame,
            obj_rect,
            scale_value,
            loops,
            pos
            # cover
        )

