import pygame as pg
from sys import exit

from loguru import logger

# import cProfile


# from memory_profiler import profile
# mprof run executable
# mprof plot

# def profile(func):
#     """Decorator for run function profile"""
#     def wrapper(*args, **kwargs):
#         profile_filename = func.__name__ + '.prof'
#         profiler = cProfile.Profile()
#         result = profiler.runcall(func, *args, **kwargs)
#         profiler.dump_stats(profile_filename)
#         return result
#     return wrapper


pg.init()


# @profile
@logger.catch
def main():
    from classes.class_Game import Game

    game = Game()
    game.run_game()


if __name__ == '__main__':
    main()
    pg.quit()
    exit()

