#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)


# создайте множество цветов, произрастающих в саду и на лугу
# garden_set = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',}
# meadow_set = {'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',}
def flover_set(txt):
    res = set(txt)
    return res


# выведите на консоль все виды цветов
def all_flover(*sets: set):
    res = ''
    i_set = 0
    flover = None
    while i_set < len(sets):
        flover = sets[0 + i_set] | sets[1 + i_set]
        i_set = i_set + 2
    for i in flover:
        res = res + i + ', '
    return res


# выведите на консоль те, которые растут и там и там
def middle_flover(*sets: set):
    res = ''
    flover = sets[0] & sets[1]
    for i in flover:
        res = res + i + ', '
    return res


# выведите на консоль те, которые растут в саду, но не растут на лугу
def only_garden_flover(flov_garden, flov_meadow):
    res = ''
    only_garden = flov_garden.difference(flov_meadow)
    for i in only_garden:
        res = res + i + ', '
    return res


# выведите на консоль те, которые растут на лугу, но не растут в саду
def only_meadow_flover(flov_garden, flov_meadow):
    res = ''
    only_meadow = flov_meadow.difference(flov_garden)
    for i in only_meadow:
        res = res + i + ', '
    return res


def main():
    garden_set = flover_set(garden)
    meadow_set = flover_set(meadow)
    alls = all_flover(garden_set, meadow_set)
    print(f'Все виды цветов: {alls[:-2]}.')
    middle = middle_flover(garden_set, meadow_set)
    print(f'Цвети которые растут и там, и там: {middle[:-2]}.')
    only_garden = only_garden_flover(garden_set, meadow_set)
    print(f'Цвети которые растут в саду, но не растут на лугу: {only_garden[:-2]}.')
    only_meadow = only_meadow_flover(garden_set, meadow_set)
    print(f'Цвети которые растут на лугу, но не растут в саду: {only_meadow[:-2]}.')


if __name__ == '__main__':
    main()
