import simple_draw as sd


def sun(pos, rad, col, ray_param=()):
    # ray_param 0 це кількість променів, а 1 це їх ширина
    center = sd.Point(*pos)
    sd.circle(center_position=center, radius=rad, color=col, width=0)
    for ray in range(0, 361, round(360 / ray_param[0])):
        star_ray = sd.Point(
            pos[0] + ((rad * 1.25) * sd.cos(ray)),
            pos[1] + ((rad * 1.25) * sd.sin(ray))
        )
        end_point = sd.Point(
            pos[0] + ((rad * 2) * sd.cos(ray)),
            pos[1] + ((rad * 2) * sd.sin(ray))
        )
        sd.line(star_ray, end_point, color=col, width=ray_param[1])

    return None


# OK
