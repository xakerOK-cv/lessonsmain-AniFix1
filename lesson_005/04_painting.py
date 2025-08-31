# -*- coding: utf-8 -*-
import simple_draw as sd

from my_package_04 import *


# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

def rectangles(start, end, color, width):
    rectangle_point = (sd.Point(*start), sd.Point(*end))
    sd.rectangle(*rectangle_point, color=color, width=width)
    return None


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

def main():
    sd.resolution = (1200, 600)

    rectangles((0, 0), (1200, 100), color=sd.COLOR_DARK_YELLOW, width=0)
    sun((110, 500), 50, sd.COLOR_YELLOW, (20, 3))
    # 0 це кількість сніжинок 1, це довжина лінії, а з 2 по 4 їхні фактори
    snow_param = (30, (10, 35), (1, 100), (10, 35), (1, 179))
    snowdrift(((95, 220), (100, 160)), many=snow_param[0], snow_param=snow_param[1:5])
    rectangles((272, 100), (775, 345), color=sd.COLOR_ORANGE, width=0)
    rectangles((272, 100), (775, 345), color=sd.COLOR_DARK_ORANGE, width=3)
    bricks((272, 769), (102, 325), length=20, width=11)
    point_list = [sd.Point(240, 345),
                  sd.Point(810, 345),
                  sd.Point(525, 400)]
    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_RED, width=0)
    rainbow_point = sd.Point(400, -300)
    round_rainbow(rainbow_point, 1000, [sd.COLOR_RED,
                                        sd.COLOR_ORANGE,
                                        sd.COLOR_YELLOW,
                                        sd.COLOR_GREEN,
                                        sd.COLOR_CYAN,
                                        sd.COLOR_BLUE,
                                        sd.COLOR_PURPLE
                                        ], thickness=12)
    tree1 = sd.Point(950, 100)
    draw_branches(tree1, 90, 100)
    tree2 = sd.Point(1100, 100)
    draw_branches(tree2, 90, 30)
    rectangles((370, 160), (490, 290), color=sd.COLOR_CYAN, width=0)
    rectangles((370, 160), (490, 290), color=sd.COLOR_DARK_YELLOW, width=3)
    smile(430, 225, sd.COLOR_YELLOW)

    # Ускладнене завдання я напевно робити не буду немає ні часу, ні сил

    sd.pause()


if __name__ == '__main__':
    main()
