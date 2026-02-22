# -*- coding: utf-8 -*-

from random import triangular

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


def chance(t_min: float, t_max: float, t_oft: float):
    if all(isinstance(x, (int, float)) for x in (t_min, t_max, t_oft)):
        return int(round(triangular(t_min, t_max, t_oft)))


def get_flakes(count: int, flakes, s_speed):
    for num in range(count):
        flakes.append(Snowflake(resolution_d=sd.resolution, color=False, num=num, s_speed=s_speed))


class Snowflake:
    def __init__(self, resolution_d, color: bool, num, s_speed=4):
        self.modifier = 0
        if color:
            self.color = sd.random_color()
        else:
            self.color = sd.COLOR_WHITE
        self.snowflake_shape = (sd.random_number(10, 100),  # length
                                sd.random_number(1, 100) / 100,  # factor_a
                                sd.random_number(10, 100) / 100,  # factor_b
                                sd.random_number(1, 179))  # factor_c
        self.point = (sd.random_number(0, resolution_d[0]),
                      sd.random_number(resolution_d[1] + self.snowflake_shape[0] + 10,
                                       resolution_d[1] + self.snowflake_shape[0] + 300))
        self.speed = s_speed

    def anim_snowflake(self):
        _point = sd.Point(self.point[0], self.point[1])
        sd.snowflake(center=_point, length=self.snowflake_shape[0],
                     color=sd.background_color, factor_a=self.snowflake_shape[1],
                     factor_b=self.snowflake_shape[2], factor_c=self.snowflake_shape[3])

        point = (self.point[0] + (chance(0.0, 5.0, 0.3) * sd.random_number(-1, 1)),
                 self.point[1] - sd.random_number(1, chance(t_min=(self.speed),
                                                            t_max=(self.speed),
                                                            t_oft=self.speed)))

        _point = sd.Point(point[0], point[1])
        sd.snowflake(center=_point, length=self.snowflake_shape[0],
                     color=self.color, factor_a=self.snowflake_shape[1],
                     factor_b=self.snowflake_shape[2], factor_c=self.snowflake_shape[3])
        return point

    def dead_snowflake(self, flakes):
        flakes.remove(self)
        get_flakes(count=1,
                   flakes=flakes,
                   s_speed=self.speed)

    def logging(self):
        print(f'Одна сніжинка, щойно зникла в пустоті.')


def main():
    n = int(input('\nВкажіть бажану кількість сніжинок:'))
    s_speed = int(input('\nВкажіть швидкість падіння (не менше 0, бажано від 5):'))

    print('\n\nПопередження: вікно з сніжинками, саме після цього не відкриється.', end='\n')
    print('Бажано почекати 5-7 циклів падіння поки сніжинки рівномірно розійдуться')
    sd.resolution = (600, 500)
    flakes = []

    # генератор сніжинок, він записує одразу в список
    get_flakes(count=n,
               flakes=flakes,
               s_speed=s_speed
               )

    while True:
        for flake in flakes[:]:
            flake.point = flake.anim_snowflake()
            if flake.point[1] <= -50 - flake.snowflake_shape[0]:
                flake.dead_snowflake(flakes)
                flake.logging()
        sd.sleep(0.018)
        if sd.user_want_exit():
            break

    # шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
    # flakes = get_flakes(count=N)  # создать список снежинок
    # while True:
    #     for flakes in flakes:
    #         flakes.clear_previous_picture()
    #         flakes.move()
    #         flakes.draw()
    #     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    #     if fallen_flakes:
    #         append_flakes(count=fallen_flakes)  # добавить еще сверху
    #     sd.sleep(0.1)
    #     if sd.user_want_exit():
    #         break

    # не бачу смислу переписувати так як я майже все зробив раніше
    # єдине що я трішки змінив кож добавивши get_flakes

    sd.pause()


if __name__ == '__main__':
    main()
