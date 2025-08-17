# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# Приклад, як було раніше в кожній функцію
# def triangle(start, angel, length):
#     start_point = sd.Point(start[0], start[1])
#
#     start_point = sd.vector(start_point, angel, length, width=2)
#     angel += round(180 - ((3 - 2) / 3 * 180), 1)
#
#     start_point = sd.vector(start_point, angel, length, width=2)
#     angel += round(180 - ((3 - 2) / 3 * 180), 1)
#
#     sd.vector(start_point, angel, length, width=2)
#     return None


def triangle(start, angel, length):
    figures(start, angel, length, 3)
    return None


def square(start, angel, length):
    figures(start, angel, length, 4)
    return None


def pentagon(start, angel, length):
    figures(start, angel, length, 5)
    return None


def hexagon(start, angel, length):
    figures(start, angel, length, 6)
    return None


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

def figures(start, angel, length, corner):
    start_point = sd.Point(start[0], start[1])

    for _ in range(corner):
        start_point = sd.vector(start_point, angel, length, width=2)
        angel += round(180 - ((corner - 2) / corner * 180), 1)

    return None


# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def main():
    sd.resolution = (700, 700)

    figure = int(input("Введіть значення:"))
    if figure == 3:
        triangle([250, 250], 0, 200)
    elif figure == 4:
        square([250, 250], 0, 200)
    elif figure == 5:
        pentagon([250, 250], 0, 200)
    elif figure == 6:
        hexagon([250, 250], 0, 200)
    else:
        print("Пропуск фігур")

    sd.pause()

    return None


if __name__ == '__main__':
    main()
