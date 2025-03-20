# -*- coding: utf-8 -*-
import copy
import simple_draw as sd


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
def bubble_default():
    position_bubble = sd.Point(sd.random_number(50, 1150), sd.random_number(50, 550))
    for radius in range(10, 21, 5):
        sd.circle(center_position=position_bubble, radius=radius, width=2)

    return

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def bubble_(point, step, size_min, size_max):
    for radius in range(size_min, size_max + 1, step):
        sd.circle(center_position=point, radius=radius, width=2)
    return

# Нарисовать 10 пузырьков в ряд
def line_bubble(y=300):
    x = 1
    old_radius = 0
    old_position = 0
    while x <= 10 :
        x += 1
        radius = sd.random_number(25, 60)
        position = sd.Point(old_position + radius, y)
        sd.circle(center_position=position, radius=radius, width=2)
        old_radius = copy.copy(radius)
        old_position += old_radius * 2
    return


# Нарисовать три ряда по 10 пузырьков
def triple_line_bubble():
    for i in range(0, 5, 2):
        line_bubble(180 + 60 * i)
    return

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def random_bubbles():
    x = 1
    while x <=100 :
        color = sd.random_color()
        if color != 'COLOR_DARK_BLUE' :
            x += 1
            sd.circle(center_position=sd.random_point(), color=color, radius=sd.random_number(20, 100), width=2)
    return


def main():
    sd.resolution = (1200, 600)

    task = int(input('Введіть номер завдання: '))

    if task == 1 :
        bubble_default()
    elif task == 2 :
        point = sd.Point(int(input('Введіть координати для x: ')), int(input('Введіть координати для y: ')))
        step = int(input('Введіть крок: '))
        size_min = int(input('Введіть мінімальний розмір: '))
        size_max = int(input('Введіть максимальний розмір: '))
        bubble_(point, step, size_min, size_max)
    elif task == 3:
        line_bubble()
    elif task == 4:
        triple_line_bubble()
    elif task == 5:
        random_bubbles()

    sd.pause()

    return


if __name__ == '__main__':
    main()
