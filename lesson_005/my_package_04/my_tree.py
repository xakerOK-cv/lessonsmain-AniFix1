import simple_draw as sd

def draw_branches(start_point, angle, length):
    color = sd.COLOR_DARK_ORANGE
    width = int(length / 10)
    if length < 4:
        return None
    if width < 2:
        color = sd.COLOR_DARK_GREEN

    start_point = sd.vector(start_point, angle, length, color=color, width=width)

    # Angle Positive and Negative
    angle_p_n = (angle + (30 + (sd.random_number(-40, 40) / 100)),
                 angle - (30 + (sd.random_number(-40, 40) / 100)))
    length *= (0.73 + (sd.random_number(-20, 20) / 100))

    for _angle in angle_p_n:
        draw_branches(start_point, _angle, length)