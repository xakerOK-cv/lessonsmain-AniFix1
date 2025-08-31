import simple_draw as sd


def round_rainbow(center, radius, color_list, thickness=1):
    for color in color_list:
        sd.circle(center, radius, color, thickness)
        radius += thickness - 1

    return
