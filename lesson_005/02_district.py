# -*- coding: utf-8 -*-
from pprint import pprint

from district.central_street.house1.room1 import folks as cf11
from district.central_street.house1.room2 import folks as cf12
from district.central_street.house2.room1 import folks as cf21
from district.central_street.house2.room2 import folks as cf22
from district.soviet_street.house1.room1 import folks as sf11
from district.soviet_street.house1.room2 import folks as sf12
from district.soviet_street.house2.room1 import folks as sf21
from district.soviet_street.house2.room2 import folks as sf22

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

rayon = ', '.join([*cf11, *cf12, *cf21, *cf22,
                   *sf11, *sf12, *sf21, *sf22], )

pprint(f'На районі живуть: {rayon}')

# OK!
