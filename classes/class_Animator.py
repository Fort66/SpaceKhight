from pygame.image import load
from pygame.transform import scale, scale_by

from os import listdir
from time import time
import numpy as np

from icecream import ic


class Animator:
    def __init__(
                self,
                dir_path=None,
                speed_frame=.05,
                obj_rect=None,
                scale_value= (1, 1),
                loops=-1,
                pos=(0, 0),
                ):


        self.dir_path = dir_path
        self.speed_frame = speed_frame
        self.scale_value = scale_value
        self.obj_rect = obj_rect
        if self.obj_rect:
            self.size = (self.obj_rect[2] * self.scale_value[0], self.obj_rect[3] * self.scale_value[1])

        self.pos = pos

        self.frames = 0
        self.frame = 0
        self.frame_time = 0
        self.loops = loops
        self.paused = False
        self.__post_init__()


    def __post_init__(self):
        self.file_list = sorted(listdir(self.dir_path))
        if self.obj_rect:
            self.original_frames = np.array([[scale(load(f'{self.dir_path}/{value}').convert_alpha(), self.size), self.speed_frame] for value in self.file_list])
        else:
            self.original_frames = np.array([[scale_by(load(f'{self.dir_path}/{value}').convert_alpha(), self.scale_value), self.speed_frame] for value in self.file_list])
        self.frames = self.original_frames.copy()
        self.rect = self.original_frames[0][0].get_rect(center=self.pos)


    def animate(self, obj_rect=None):
        self.obj_rect = obj_rect
        if self.obj_rect:
            self.size = (self.obj_rect[2] * self.scale_value[0], self.obj_rect[3] * self.scale_value[1])

        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time > self.frames[self.frame][1]:
            if self.loops == -1:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
                self.frame_time = time()
                self.update_frames()

            if self.loops > 0:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else self.frames[-1]
                self.frame_time = time()
                self.update_frames()
                if self.frame == len(self.frames) - 1:
                    self.loops -= 1

    def update_frames(self):
        if self.loops:
            self.frames[self.frame][0] = self.original_frames[self.frame][0].copy()
            if self.obj_rect:
                self.frames[self.frame][0] = scale(self.frames[self.frame][0], self.size)
            else:
                self.frames[self.frame][0] = scale_by(self.frames[self.frame][0], self.scale_value)






