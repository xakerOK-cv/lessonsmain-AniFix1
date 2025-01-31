#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Есть значение радиуса круга
radius = 42


# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

def area(rad):
    res = round(3.1415926 * rad ** 2, 4)
    return res


# Далее, пусть есть координаты точки
point_1 = (23, 34)


# где 23 - координата х, 34 - координата у

# Если точка point_1 лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

def point_in_a_circle(point_x, point_y, radius_circle=None):
    loong = math.sqrt(point_x ** 2 + point_y ** 2)
    if radius_circle is not None:
        res = loong >= radius_circle
        return res
    else:
        return loong


# Аналогично для другой точки
point_2 = (30, 30)


# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.


def main():
    print(f'\nПлоща кола з радіусом {radius}см дорівнює {area(radius)}см{chr(0x00B2)}.')

    print(f'\nЧи знаходиться точка {point_1} в колі?(Довжина точки: '
          f'{round(point_in_a_circle(point_1[0], point_1[-1]), 2)} см) '
          f'\n {point_in_a_circle(point_1[0], point_1[-1], radius)}')

    print(f'\nЧи знаходиться точка {point_2} в колі?(Довжина точки:'
          f' {round(point_in_a_circle(point_2[0], point_2[-1]), 2)}см) '
          f'\n {point_in_a_circle(point_2[0], point_2[-1], radius)}')


# Пример вывода на консоль:
#
# 77777.7777
# False
# False


if __name__ == "__main__":
    main()
