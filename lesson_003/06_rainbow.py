# -*- coding: utf-8 -*-
# python 3.8

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

Point_1 = [50, 50]
Point_2 = [350, 450]


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def seven_lines(start_point, end_point, color_list, step, thickness=1):
    for color in color_list:
        start = sd.Point(start_point[0], start_point[1])
        end = sd.Point(end_point[0], end_point[1])
        sd.line(start, end, color, thickness)
        start_point[0] += step
        end_point[0] += step

    return


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
def round_rainbow(center, radius, color_list, thickness=1):
    for color in color_list:
        sd.circle(center, radius, color, thickness)
        radius -= thickness - 1

    return


def main():
    x = int(input('input : '))
    sd.resolution = (500, 500)
    if x == 1:
        seven_lines(Point_1, Point_2, rainbow_colors, 5, 4)
    elif x == 0:
        round_rainbow(sd.Point(550, -100), 620, rainbow_colors, 35)
    sd.pause()


if __name__ == '__main__':
    main()
