import simple_draw as sd

def snowdrift(rang = (), many:int = 0, snow_param=()):
    snowflake_point = [(sd.random_number(*rang[0]),
                        sd.random_number(*rang[1]))
                       for _ in range(many)]

    # Через assert, я не можу зробити діапазон від 10 до 100 тому, я зробив так, як я зрозумів це проценти від довжини
    # та кут. Знизу частина коду сніжинки.
    # assert 0 < factor_a <= 1 - место ответвления лучиков
    # assert 0 < factor_b <= 1 - длина лучиков
    # assert 0 < factor_c < 180 - угол отклонения лучиков

    snowflake_shape = [(sd.random_number(*snow_param[0]),  # length
                        sd.random_number(*snow_param[1]) / 100,  # factor_a
                        sd.random_number(*snow_param[2]) / 100,  # factor_b
                        sd.random_number(*snow_param[3]))  # factor_c
                       for _ in range(many)]

    for i in range(many):
        pre_snowflake_point = sd.Point(snowflake_point[i][0], snowflake_point[i][1])
        sd.snowflake(center=pre_snowflake_point, length=snowflake_shape[i][0],
                     color=sd.COLOR_WHITE, factor_a=snowflake_shape[i][1],
                     factor_b=snowflake_shape[i][2], factor_c=snowflake_shape[i][3])

    return None