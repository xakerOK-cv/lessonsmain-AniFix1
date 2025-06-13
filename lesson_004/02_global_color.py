# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def triangle(start, angel, length, color):
    figures(start, angel, length, 3, color)
    return None


def square(start, angel, length, color):
    figures(start, angel, length, 4, color)
    return None


def pentagon(start, angel, length, color):
    figures(start, angel, length, 5,color)
    return None


def hexagon(start, angel, length, color):
    figures(start, angel, length, 6, color)
    return None


def figures(start, angel, length, corner, color):
    start_point = sd.Point(start[0], start[1])

    for _ in range(corner):
        start_point = sd.vector(start_point, angel, length, color=color, width=2)
        angel += round(180 - ((corner - 2) / corner * 180), 1)

    return None



# Костиль номер 1
COLOR = ( sd.COLOR_WHITE, sd.COLOR_BLACK, sd.COLOR_RED,
sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE,
sd.COLOR_DARK_YELLOW, sd.COLOR_DARK_ORANGE, sd.COLOR_DARK_RED,
sd.COLOR_DARK_GREEN, sd.COLOR_DARK_CYAN, sd.COLOR_DARK_BLUE,
sd.COLOR_DARK_PURPLE )

# Костиль номер 2
color_name = ( '0 COLOR_WHITE', '1 COLOR_BLACK', '2 COLOR_RED',
'3 COLOR_ORANGE', '4 COLOR_YELLOW', '5 COLOR_GREEN',
'6 COLOR_CYAN', '7 COLOR_BLUE', '8 COLOR_PURPLE',
'9 COLOR_DARK_YELLOW', '10 COLOR_DARK_ORANGE', '11 COLOR_DARK_RED',
'12 COLOR_DARK_GREEN', '13 COLOR_DARK_CYAN', '14 COLOR_DARK_BLUE',
'15 COLOR_DARK_PURPLE' )



def main():
    sd.resolution = (700, 700)

    figure = int(input("Введіть значення:"))
    print('\n', *color_name, sep='\n', end='\n\n\n')
    color = int(input("Напишіть номер кольора фігури:"))
    if figure == 3:
        triangle([250, 250], 0, 200, COLOR[color])
    elif figure == 4:
        square([250, 250], 0, 200, COLOR[color])
    elif figure == 5:
        pentagon([250, 250], 0, 200, COLOR[color])
    elif figure == 6:
        hexagon([250, 250], 0, 200, COLOR[color])
    else:
        print("Таких фігур ненайденно")

    sd.pause()


if __name__ == '__main__':
    main()