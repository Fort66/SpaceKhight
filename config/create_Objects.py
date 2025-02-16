from UI.Screens.class_ScreenGame import ScreenGame
from classes.class_SpriteGroups import SpriteGroups


screen = ScreenGame(
                    size = (1280, 720),
                    caption = 'Game',
                    color = 'SteelBlue',
                    icon = '',
                    is_resizable = True,
                    is_full_screen = False
                    )


sprite_groups = SpriteGroups()