import simple_draw as sd


def bricks(point_x, point_y, length, width):
    mod = 0
    side = 0
    for row in range(*point_x, int(length / 2)):
        # це все знизу один великий костиль на який я вбив 3 години
        if side:
            width = width * -1
            mod = abs(width * 2)

        for brick in range(*point_y, abs(width) * 2):
            points = [sd.Point(row + (length / 2), brick + mod),
                      sd.Point(row + (length / 2), brick + width + mod),
                      sd.Point(row, brick + width + mod),
                      sd.Point(row, brick + width * 2 + mod),
                      sd.Point(row + (length / 2), brick + width * 2 + mod)]
            for i in range(1, 5):
                sd.line(points[i - 1], points[i], sd.COLOR_DARK_ORANGE, 2)
        if side:
            width = width * -1
            mod = 0
            side = 0
        else:
            side = 1
