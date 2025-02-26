import pygame as pg
from sys import exit

from loguru import logger

# import cProfile
# import pstats


# from memory_profiler import profile
# mprof run executable
# mprof plot

# def profile(func):
#     """Decorator for run function profile"""
#     def wrapper(*args, **kwargs):
#         profile_filename = func.__name__ + '.txt'
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



if __name__ == "__main__":
    # with cProfile.Profile() as pr:
    main()
        # with open( 'profile.txt', 'w+' ) as f:
        #     pstats.Stats( pr, stream=f ).strip_dirs().sort_stats("cumtime").print_stats()

    pg.quit()
    exit()


# import pstats

# with cProfile.Profile() as pr:
#   my_func_to_be_profiled()
#   with open( 'output_filename.txt', 'w' ) as f:
#     pstats.Stats( pr, stream=f ).strip_dirs().sort_stats("cumtime").print_stats()