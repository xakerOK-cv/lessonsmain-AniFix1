# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:

    def __str__(self):
        return 'Воды'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Par(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Griaz(part1=self, part2=other)



class Air:

    def __str__(self):
        return 'Воздуха'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lithing(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Pil(part1=self, part2=other)
        elif isinstance(other, Water):
            return Storm(part1=self, part2=other)


class Fire:

    def __str__(self):
        return 'Огня'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Water):
            return Par(part1=self, part2=other)
        elif isinstance(other, Air):
            return Lithing(part1=self, part2=other)
        elif isinstance(other, Love):
            return Life(part1=self, part2=other)


class Earth:

    def __str__(self):
        return 'Земли'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Water):
            return Griaz(part1=self, part2=other)
        elif isinstance(other, Air):
            return Pil(part1=self, part2=other)


class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я Шторм. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Par:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я Пар. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Griaz:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я грязь. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Lithing:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я молния. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Pil:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я пыль. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я лава. Состою из ' + str(self.part1) + ' и ' + str(self.part2)

class Love:

    def __str__(self):
        return 'Любовь'

    def __add__(self, other):
            return Life(part1=self, part2=other)

class Life:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я жизнь. Состою из ' + str(self.part1) + ' и ' + str(self.part2)



water = Water()
air = Air()
fire = Fire()
earth = Earth()

result = water + air
print(result)
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Love(), '=', Fire() + Love())



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
