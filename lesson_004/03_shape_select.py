# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


FIGURE = ('Triangle', 'Square', 'Pentagon', 'Hexagon')


def main():
    sd.resolution = (700, 700)

    print('\n', *FIGURE, sep='\n', end='\n\n\n')
    figure = input("Скопіюйте назву фігури:")
    print('\n', *color_name, sep='\n', end='\n\n\n')
    color = int(input("Напишіть номер кольора фігури:"))
    if figure == 'Triangle':
        triangle([250, 250], 0, 200, COLOR[color])
    elif figure == 'Square':
        square([250, 250], 0, 200, COLOR[color])
    elif figure == 'Pentagon':
        pentagon([250, 250], 0, 200, COLOR[color])
    elif figure == 'Hexagon':
        hexagon([250, 250], 0, 200, COLOR[color])
    else:
        print("Таких фігур ненайденно")

    sd.pause()


if __name__ == '__main__':
    main()

sd.pause()
