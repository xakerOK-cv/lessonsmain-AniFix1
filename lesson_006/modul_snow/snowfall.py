# -*- coding: utf-8 -*-

import simple_draw as sd


def anim_snowflake(point, color, length, factors, rand, speed):
    _point = sd.Point(point[0], point[1])
    sd.snowflake(center=_point, length=length,
                 color=sd.background_color, factor_a=factors[0],
                 factor_b=factors[1], factor_c=factors[2])

    random_index = sd.random_number(0, 19)

    point = (point[0] + (rand[random_index] * sd.random_number(-1, 1)),
             point[1] - sd.random_number(1, speed))

    _point = sd.Point(point[0], point[1])
    sd.snowflake(center=_point, length=length,
                 color=color, factor_a=factors[0],
                 factor_b=factors[1], factor_c=factors[2])
    return point


def clear_snowflake(snowflake_num, point_list, shape_list):
    shape_list[snowflake_num] = (sd.random_number(10, 100), sd.random_number(1, 100) / 100,
                                 sd.random_number(10, 100) / 100, sd.random_number(1, 179))

    point_list[snowflake_num] = (sd.random_number(0, 500),
                                 sd.random_number(600 + shape_list[snowflake_num][0],
                                                  700 + shape_list[snowflake_num][0])
                                 , sd.random_color())


def logging(snow_num):
    print(f'{snow_num} зникла в пустоті')
