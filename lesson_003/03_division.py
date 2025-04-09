# -*- coding: utf-8 -*-
from decimal import Decimal

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37


def division(number_1, number_2):
    res = 0
    i = 3
    x = 1.0
    while i > 0:
        if number_1 > 0:
            if isinstance(number_1, int) and number_1 - number_2 > 0:
                number_1 -= number_2
                res += 1 * Decimal(x)
            else:
                number_1 *= 10
                x *= 0.1
                i -= 1
        else:
            break
    return round(res, 2)


def main():
    print(f'Ділення числа {a} на {b} дає {division(a, b)}')
    return


if __name__ == '__main__':
    main()


# isinstance так один з гарних варіантів, 0 < i < 1 
# OK
