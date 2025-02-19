from UI.Screens.class_ScreenGame import ScreenGame
from logic.class_Checks import Checks
from config.sources.class_Weapons import Weapons



screen = ScreenGame(
    size=(1280, 720),
    caption="Game",
    color="SteelBlue",
    icon="",
    is_resizable=True,
    is_full_screen=False,
)


checks = Checks()
weapons = Weapons()