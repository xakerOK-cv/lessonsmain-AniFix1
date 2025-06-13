# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# def draw_branches(start_point, angle, length):
#     start_point = sd.vector(start_point, angle, length)
#     angle += 30
#     sd.vector(start_point, angle, length)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# def draw_branches(start_point, angle, length):
#     if length < 3 :
#         return None
#     start_point = sd.vector(start_point, angle, length)
#     angle_p_n = angle + 30, angle - 30
#     length *= 0.75
#     for _angle in angle_p_n:
#         draw_branches(start_point, _angle, length)



# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(start_point, angle, length):
    if length < 4 :
        return None
    start_point = sd.vector(start_point, angle, length)

    # Angle Positive and Negative
    angle_p_n = ( angle + (30 + (sd.random_number(-40, 40) / 100)),
                  angle - (30 + (sd.random_number(-40, 40) / 100)) )
    length *= (0.75 + (sd.random_number(-20, 20) / 100))

    for _angle in angle_p_n:
        draw_branches(start_point, _angle, length)

def main():
    sd.resolution = (700, 750)

    root_point = sd.Point(350, 30)
    draw_branches(start_point=root_point, angle=90, length=100)


    sd.pause()


if __name__ == '__main__':
    main()