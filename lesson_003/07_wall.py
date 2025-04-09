# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

def bricks(length, width):
    for row in range(0, 601, int(length / 2)):
        for brick in range(0, 601, width * 2):
            if not row % 100 == 0:
                brick -= width
            points = [sd.Point(row + (length / 2), brick),
                      sd.Point(row + (length / 2), brick + width),
                      sd.Point(row, brick + width),
                      sd.Point(row, brick + width * 2),
                      sd.Point(row + (length / 2), brick + width * 2)]
            for i in range(1, 5):
                sd.line(points[i - 1], points[i], sd.COLOR_DARK_YELLOW, 2)


def main():
    sd.resolution = (600, 600)

    bricks(100, 50)
    sd.pause()
    return


if __name__ == '__main__':
    main()


# стіна нормас)