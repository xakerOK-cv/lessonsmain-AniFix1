# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

def anim_snowflake(point, length, factors, rand, speed):
    _point = sd.Point(point[0], point[1])
    sd.snowflake(center=_point, length=length,
                 color=sd.background_color, factor_a=factors[0],
                 factor_b=factors[1], factor_c=factors[2])

    random_index = sd.random_number(0, 19)

    point = (point[0] + (rand[random_index] * sd.random_number(-1, 1)),
             point[1] - sd.random_number(1, speed))

    _point = sd.Point(point[0], point[1])
    sd.snowflake(center=_point, length=length,
                 color=sd.COLOR_WHITE, factor_a=factors[0],
                 factor_b=factors[1], factor_c=factors[2])
    return point

def clear_snowflake(snowflake_num, point_list, shape_list):
    shape_list[snowflake_num] = (sd.random_number(10, 100), sd.random_number(1, 100) / 100,
                                 sd.random_number(10, 100) / 100, sd.random_number(1, 179))

    point_list[snowflake_num] = (sd.random_number(0, 500),
                                 sd.random_number(600+shape_list[snowflake_num][0],
                                                  700+shape_list[snowflake_num][0]))

def wind_generate():


    return

def main():
    sd.resolution = (600, 500)
    N = 20

    # Це список для створення вірогідності(0=55%, 1=25%, 2=15%, 3=5%)
    rand_num_list = [0,0,0,0,0,0,0,1,1,2,
                     0,0,0,0,0,1,1,2,2,3]

    # Все до циклу while це рендер першого кадру, основи для анімації.

    snowflake_point = [(sd.random_number(0, 600),
                       sd.random_number(0, 500))
                       for _ in range(N)]

    # Через assert, я не можу зробити діапазон від 10 до 100 тому, я зробив так, як я зрозумів це проценти від довжини
    # та кут. Знизу частина коду сніжинки.
    # assert 0 < factor_a <= 1 - место ответвления лучиков
    # assert 0 < factor_b <= 1 - длина лучиков
    # assert 0 < factor_c < 180 - угол отклонения лучиков

    snowflake_shape = [(sd.random_number(10, 100), # length
                        sd.random_number(1, 100) / 100, # factor_a
                        sd.random_number(10, 100) / 100, # factor_b
                        sd.random_number(1, 179)) # factor_c
                       for _ in range(N)]


    for i in range(N):
        pre_snowflake_point = sd.Point(snowflake_point[i][0], snowflake_point[i][1])
        sd.snowflake(center=pre_snowflake_point, length=snowflake_shape[i][0],
                     color=sd.COLOR_WHITE, factor_a=snowflake_shape[i][1],
                     factor_b=snowflake_shape[i][2], factor_c=snowflake_shape[i][3])

    # Основний цикл

    while True:
        sd.start_drawing()

        for snow_num in range(N) :
            snowflake_point[snow_num] = anim_snowflake(point=snowflake_point[snow_num],
                                                       length=snowflake_shape[snow_num][0],
                                                       factors=(
                                                                snowflake_shape[snow_num][1],
                                                                snowflake_shape[snow_num][2],
                                                                snowflake_shape[snow_num][3]
                                                                ),
                                                       rand=rand_num_list, speed=4)

            if snowflake_point[snow_num][1] <= -40 - snowflake_shape[snow_num][0] :
                clear_snowflake(snow_num, snowflake_point, snowflake_shape)

        sd.finish_drawing()
        sd.sleep(0.02)
        if sd.user_want_exit():
            break
    sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку


if __name__ == '__main__':
    main()
