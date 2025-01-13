#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Есть словарь координат городов


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

DataUserKeys = str(input('Введіть назву міста відстань до якого '
                         f'ви хочете дізнатися (доступно {list(sites.keys())})'
                         f'\nВвод: '))

Coordinates = []

try:
    sites[DataUserKeys]
except KeyError:
    print('Перевірте місто, що ви ввели, можливо ви'
          ' опечатались або в нас не має цього міста.')
    print(f'Ви ввели: {DataUserKeys}\nДоступні у нас {list(sites.keys())}')
else:
    for i in sites.keys():
        Coordinates = sites[i]
        UserCoordinates = sites[DataUserKeys]
        x1 = UserCoordinates[0]
        y1 = UserCoordinates[1]
        x2 = Coordinates[0]
        y2 = Coordinates[1]
        res = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 1)
        distances.setdefault(i, res)
    distances.pop(DataUserKeys)
    for item in distances.items():
        print(item)




