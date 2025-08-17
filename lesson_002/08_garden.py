#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу ТУТ СУПЕР
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов СУПЕР
All_flowers_set = garden_set | meadow_set
print(All_flowers_set)


# выведите на консоль те, которые растут и там и там СУПЕР
All_flowers_set2 = garden_set & meadow_set
print(All_flowers_set2)

# выведите на консоль те, которые растут в саду, но не растут на лугу СУПЕР
Garden_flowers = garden_set - meadow_set
print(Garden_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду СУПЕР
Meadow_flowers = meadow_set - garden_set
print(Meadow_flowers)


