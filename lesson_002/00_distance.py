#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Есть словарь координат городов


sites = {
    'Kiev': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# Запит у користувача міста від якого потрібно вирахувати відстань

DataUserKeys = str(input('Введіть назву міста відстань до якого '
                         f'ви хочете дізнатися (доступно {list(sites.keys())})'
                         f'\nВвод: '))

Coordinates = []

# Перевірка чи є в словарю цей ключ(місто)

try:
    sites[DataUserKeys]
except KeyError:
    print('Перевірте місто, що ви ввели, можливо ви'
          ' опечатались або в нас не має цього міста.')
    print(f'Ви ввели: {DataUserKeys}\nДоступні у нас {list(sites.keys())}')
else:
    # Якщо є, то виповняються наступні команди
    for i in sites.keys():
        # В список Coordinates та UserCoordinates записуються данні по ключам
        Coordinates = sites[i]
        UserCoordinates = sites[DataUserKeys]
        # Переписуються потрібні данні в потрібні перемінні для мат. операцій
        x1 = UserCoordinates[0]
        y1 = UserCoordinates[1]
        x2 = Coordinates[0]
        y2 = Coordinates[1]
        # В перемінну записується математична операція. Після чого з потрібним ключем записали потрібні данні.
        res = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 1)
        distances.setdefault(i, res)
    # Видалення безкорисних результатів
    distances.pop(DataUserKeys)
    # Спроба гарно вивести значення
    for item in distances.items():
        print(f'Від {DataUserKeys} До {item[0]}: {item[1]} Кілометрів')

     # В цілому все супер)) 
