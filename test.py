# import os
# import pygame
# from pygame.sprite import Sprite
# from math import radians, sin, cos
# from icecream import ic
  
# class Scene:
#     def on_draw( surface): pass
#     def on_event( event): pass
#     def on_update( delta): pass
  
# class Manager:
#     def __init__( caption, width, height, center=True):
#         if center:
#             os.environ['SDL_VIDEO_CENTERED'] = '1'
  
#         # Basic pygame setup
#         pygame.display.set_caption(caption)
#         surface = pygame.display.set_mode((width, height))
#         rect = surface.get_rect()
#         clock = pygame.time.Clock()
#         running = False
#         delta = 0
#         fps = 600
  
#         # Scene Interface
#         scene = Scene()
  
#     def mainloop(:
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 scene.on_event(event)
  
#             scene.on_update(delta)
#             scene.on_draw(surface)
#             pygame.display.flip()
#             delta = clock.tick(fps)
  
# class BaseSprite(Sprite):
#     def __init__( image, position, anchor="topleft"):
#         Sprite.__init__(
#         original_image = image
#         image = image
#         rect = image.get_rect()
#         setattr(rect, anchor, position)
  
#     def draw( surface):
#         surface.blit(image, rect)
  
# class RotationMovementKeys:
#     def __init__( sprite, up, down, left, right):
#         sprite = sprite
#         up = up
#         down = down
#         left = left
#         right = right
  
#         angle = 0
#         speed = 0.04
#         rotation_speed = 0.08
#         center = pygame.Vector2(sprite.rect.center)
#         set_direction()
  
#     def set_direction(:
#         rad = radians(angle)
#         direction = pygame.Vector2(sin(rad), cos(rad))
  
#     def do_rotate(:
#         ic(angle)
#         sprite.image = pygame.transform.rotate(sprite.original_image, angle)
#         sprite.rect = sprite.image.get_rect()
#         sprite.rect.center = center
#         set_direction()
  
#     def on_keydown( keys_press, delta):
#         if keys_press[up]:
#             center -= direction * delta * speed
#             sprite.rect.center = center
#         elif keys_press[down]:
#             center += direction * delta * (speed / 2)
#             sprite.rect.center = center
  
#         if keys_press[right]:
#             angle = (angle - rotation_speed * delta) % 360
#             do_rotate()
#         elif keys_press[left]:
#             angle = (angle + rotation_speed * delta) % 360
#             do_rotate()
  
# class Example(Scene):
#     def __init__( manager):
#         create_image()
#         manager = manager
#         sprite = BaseSprite(rectangle, manager.rect.center, "center")
#         sprite_movement = RotationMovementKeys(sprite,
#             pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
  
#     def create_image(:
#         rectangle = pygame.Surface((10, 20), pygame.SRCALPHA)
#         rectangle.fill(pygame.Color('dodgerblue'))
#         rectangle.fill(pygame.Color('white'), (2, 2, 6, 3))
  
#     def on_draw( surface):
#         surface.fill(pygame.Color("black"))
#         sprite.draw(surface)
  
#     def on_event( event):
#         if event.type == pygame.QUIT:
#             manager.running = False
  
#     def on_update( delta):
#         keys = pygame.key.get_pressed()
#         sprite_movement.on_keydown(keys, delta)
  
# def main():
#     pygame.init()
#     manager = Manager("Rotation Example", 800, 600)
#     manager.scene = Example(manager)
#     manager.mainloop()
  
# if __name__ == "__main__":
#     main()

import pygame, sys, gif_pygame
from gif_pygame.transform import scale, flip, rotate, rotozoom, scale_by
from pygame.image import load
from icecream import ic

from loguru import logger

import fnmatch
import os

from units.class_Guardian import Animator
# dir_path = 'images/Guards/guard1'
# file_list = os.listdir(dir_path)
# # ic(file_list)
# count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
# print('Количество файлов:', count)

win = pygame.display.set_mode((512, 512))
# example_gif = gif_pygame.load("images/Guards/guard1.gif") # Loads a .gif file
# example_png = gif_pygame.load("example.png") # Loads a .png file, the module supports non-animated files, but it is not recommended

# s1 = pygame.Surface((66, 66))
# s2 = pygame.Surface((66, 66))
# s3 = pygame.Surface((66, 66))
# s1.fill((255, 0, 0))
# s2.fill((0, 255, 0))
# s3.fill((0, 0, 255))

# example_surfs = gif_pygame.GIFPygame([(s1, 1), (s2, 1), (s3, 1)])

# guardian = [[load(f'images/Guards/guard1/{i}.png').convert_alpha(), .05] for i in range(count - 1)]

# guardian = [[load(f'{dir_path}/{value}').convert_alpha(), .05] for value in file_list]
# guardian_rect = guardian[0][0].get_rect(center=(256, 256))

clock = pygame.Clock()

# import time

# orig_frames = guardian.copy()
# frames = guardian.copy()

# frame = 0
# frame_time = 0
# paused_time = 0
# paused = False
# loops = [0, -1]
# ended = False

# @logger.catch
# def animate():
#     global frame, frame_time, paused_time, paused, loops, ended
#     if frame_time == 0:
#         frame_time = time.time()

#     if time.time()-frame_time >= frames[frame][1] and not paused and not ended:
#         frame = frame + 1 if frame < len(frames)-1 else 0
#         frame_time = time.time()
#         if frame >= len(frames)-1:
#             loops[0] += 1
        
    # if loops[1] != -1 and loops[0] > loops[1]:
    #     ended = True
    #     # pause()
    #     paused = False
        
    # win.blit(frames[frame][0], guardian.rect)


animation = Animator('images/Guards/guard2', .09, win.get_rect().center)


while True:
    clock.tick(100)
    win.fill((0, 0, 0))
    
    # There are 2 ways of rendering the animated img file, the first method is doing "gif.render(surface, (x, y))", the other method is doing "surface.blit(gif.blit_ready(), (x, y))". THE ".blit_ready()" FUNCTION MUST BE CALLED WHEN DOING THE SECOND METHOD
    # example_gif.render(win, (example_gif.get_width()*.35, example_gif.get_height()*0.35))
    # guardian.render(win, guardian_rect)
    # win.blit(example_surfs.blit_ready(), (384-example_surfs.get_width()*0.5, 256-example_surfs.get_height()*0.5))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
                # if example_gif.paused: # Check whether `example_gif` is paused or not
                #     example_gif.unpause() # unpauses `example_gif` if it was paused
                # else:
                #     example_gif.pause() # pauses `example_gif` if it was unpaused

                # if example_png.paused: # Check whether `example_png` is paused or not, since this is a non-animated image, it will not be affected
                #     example_png.unpause() # unpauses `example_png` if it was paused, since this is a non-animated image, it will not be affected
                # else:
                #     example_png.pause() # pauses `example_png` if it was unpaused, since this is a non-animated image, it will not be affected

                # if guardian.paused: # Check whether `example_surfs` is paused or not
                #     guardian.unpause() # unpauses `example_surfs` if it was paused
                # else:
                #     guardian.pause() # pauses `example_surfs` if it was unpaused
    # animation.animate(win)
    animation.animate()
    # win.blit(frames[frame][0], guardian_rect)
    win.blit(animation.frames[animation.frame][0], animation.rect)
    pygame.display.flip()

