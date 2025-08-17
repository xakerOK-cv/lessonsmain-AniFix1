# -*- coding: utf-8 -*-
import room_1
import room_2

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

rayon = ', '.join([*room_1.folks, *room_2.folks], )

print(f'На районі живуть: {rayon}')
