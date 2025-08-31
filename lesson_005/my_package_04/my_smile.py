import simple_draw as sd

def smile(coordinate_x, coordinate_y, color=None):
    if color is None:
        exit()
    smile_coordinate = [sd.Point(coordinate_x - 50, coordinate_y - 45),
                        sd.Point(coordinate_x + 50, coordinate_y + 45)]

    sd.ellipse(smile_coordinate[0], smile_coordinate[1], color)

    eye_smile = [sd.Point((coordinate_x - 25) - 7, (coordinate_y + 16) - 7),
                 sd.Point((coordinate_x - 25) + 7, (coordinate_y + 16) + 7),
                 sd.Point((coordinate_x + 25) - 7, (coordinate_y + 16) - 7),
                 sd.Point((coordinate_x + 25) + 7, (coordinate_y + 16) + 7), ]

    random_color = sd.COLOR_DARK_CYAN


    while random_color == color:
        random_color = sd.random_color()
    sd.ellipse(eye_smile[0], eye_smile[1], random_color)
    sd.ellipse(eye_smile[2], eye_smile[3], random_color)
    coordinate_list = []
    radius = 25

    for angle in range(-57, 57):
        coo_1 = coordinate_x + (radius * sd.cos((angle + 270))) * 1.1
        coo_2 = coordinate_y + (radius * sd.sin((angle + 270)))
        coordinate_list.append(sd.Point(coo_1, coo_2))

    sd.lines(coordinate_list, random_color, width=4)

    return
