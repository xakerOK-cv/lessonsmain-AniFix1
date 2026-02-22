# -*- coding: utf-8 -*-

import simple_draw as sd
from modul_snow import snowfall as sf

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


def main():
    n = int(input('Бажана кількість сніжинок (Попередження: вікно з сніжинками саме після цього не відкриється):'))
    sd.resolution = (600, 500)

    # Це список для створення вірогідності(0=55%, 1=25%, 2=15%, 3=5%)
    rand_num_list = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
                     0, 0, 0, 0, 0, 1, 1, 2, 2, 3]

    # Все до циклу while це рендер першого кадру, основи для анімації.

    snowflake_point_and_color = [(sd.random_number(0, 600),
                                  sd.random_number(0, 500), sd.random_color())
                                 for _ in range(n)]

    # Через assert, я не можу зробити діапазон від 10 до 100 тому, я зробив так, як я зрозумів це проценти від довжини
    # та кут. Знизу частина коду сніжинки.
    # assert 0 < factor_a <= 1 - место ответвления лучиков
    # assert 0 < factor_b <= 1 - длина лучиков
    # assert 0 < factor_c < 180 - угол отклонения лучиков

    snowflake_shape = [(sd.random_number(10, 100),  # length
                        sd.random_number(1, 100) / 100,  # factor_a
                        sd.random_number(10, 100) / 100,  # factor_b
                        sd.random_number(1, 179))  # factor_c
                       for _ in range(n)]

    for i in range(n):
        pre_snowflake_point = sd.Point(snowflake_point_and_color[i][0], snowflake_point_and_color[i][1])
        sd.snowflake(center=pre_snowflake_point, length=snowflake_shape[i][0],
                     color=snowflake_point_and_color[i][2], factor_a=snowflake_shape[i][1],
                     factor_b=snowflake_shape[i][2], factor_c=snowflake_shape[i][3])

    # Основний цикл

    while True:
        sd.start_drawing()

        # Новий костиль
        for snow_num in range(n):
            snow_color = snowflake_point_and_color[snow_num][2]
            snowflake_point_and_color[snow_num] = *sf.anim_snowflake(point=snowflake_point_and_color[snow_num][:2],
                                                                  color=snowflake_point_and_color[snow_num][2],
                                                                  length=snowflake_shape[snow_num][0],
                                                                  factors=(
                                                                      snowflake_shape[snow_num][1],
                                                                      snowflake_shape[snow_num][2],
                                                                      snowflake_shape[snow_num][3]
                                                                  ),
                                                                  rand=rand_num_list, speed=4), snow_color

            if snowflake_point_and_color[snow_num][1] <= -40 - snowflake_shape[snow_num][0]:
                sf.clear_snowflake(snow_num, snowflake_point_and_color, snowflake_shape)
                sf.logging(snow_num)

        sd.finish_drawing()
        sd.sleep(0.018)
        if sd.user_want_exit():
            break
    sd.pause()

    sd.pause()


if __name__ == '__main__':
    main()