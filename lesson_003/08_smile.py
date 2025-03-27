# -*- coding: utf-8 -*-
import math
from random import randrange

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(coordinate_x, coordinate_y, color=sd.COLOR_YELLOW):
    smile_coordinate = [sd.Point(coordinate_x-50, coordinate_y-45),
                        sd.Point(coordinate_x+50,coordinate_y+45)]
    sd.ellipse(smile_coordinate[0], smile_coordinate[1], color)
    eye_smile = [sd.Point((coordinate_x-25)-7, (coordinate_y+16)-7),
                 sd.Point((coordinate_x-25)+7, (coordinate_y+16)+7),
                 sd.Point((coordinate_x+25)-7, (coordinate_y+16)-7),
                 sd.Point((coordinate_x+25)+7, (coordinate_y+16)+7),]
    random_color = sd.COLOR_DARK_CYAN
    while random_color == color:
        random_color = sd.random_color()
    sd.ellipse(eye_smile[0], eye_smile[1], random_color)
    sd.ellipse(eye_smile[2], eye_smile[3], random_color)
    coordinate_list = []
    # Зроблено з підказкою від чата гпт
    radius = 25
    for angle in range(-57, 57):
        coo_1 = coordinate_x + (radius * math.cos(math.radians(angle + 270))) * 1.1
        coo_2 = coordinate_y + (radius * math.sin(math.radians(angle + 270)))
        coordinate_list.append(sd.Point(coo_1, coo_2))

    # 2. Ще одна не вдала спроба

    # bank = 1
    # coo_1 = []
    # for i in range(-15):
    #     bank *= 1.02
    #     coo_1 += [[round(coordinate_x + round(abs(i)) * (-1 if i < 0 else 1)),
    #            (coordinate_y - 20) + round((abs(i) * bank)/10)]]
    # bank = 1
    # coo_2 = []
    # for i in range(16):
    #     bank *= 1.02
    #     coo_1 += [[round(coordinate_x + round(abs(i)) * (-1 if i < 0 else 1)),
    #                (coordinate_y - 20) + round((abs(i) * bank) / 10)]]
    # coordinate_list.extenad(coo_1,coo_2)


    # 1. Хотів зробити гарно, а вийшло, як завжди(не звертайте увагу воно просто їснує, і щось робить)

    # x = 2
    # coordinate_list = [[round(coordinate_x+i),
    #                     (coordinate_y-20)+round(x**1.08)] for i in range(-19, 20)]
    #
    # for index, coordinate in enumerate(coordinate_list):
    #     coordinate_list[index] = sd.Point(coordinate[0], coordinate[1])

    sd.lines(coordinate_list, random_color, width=4)
    return

def main():
    sd.resolution = (1000, 700)
    for i in range(10):
        x = randrange(0, 1000)
        y = randrange(0, 700)
        smile(x, y, sd.COLOR_GREEN)
    sd.pause()
    return

if __name__ == '__main__':
    main()