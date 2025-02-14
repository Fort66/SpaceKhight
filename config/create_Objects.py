'''
Этот файл для создания объектов (экземпляров классов) для того, чтобы максимально избежать циклического импорта
'''
# import sys
# print(sys.path)


from UI.Screens.class_ScreenGame import ScreenGame


# экземпляр класса ScreenGame (окно игры)
screen = ScreenGame(size = (1280, 720),
                    caption = 'Game',
                    color = 'SteelBlue',
                    icon = '', # пример иконки
                    is_resizable = True, # изменяемый размер True/False
                    is_full_screen = False) #полноэкранный True/False

