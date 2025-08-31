# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:

# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger

# 1
# my_burger.double_cheeseburger()

# 2
push = None
while not push:
    ingredients = ['булочки', 'котлеты', 'огурчика',
                   'помидорчика', 'майонеза', 'сыра', ]
    for index, ingredient in enumerate(ingredients):
        print(f'{index}. {ingredient}')
    user = int(input('Введіть номер інгредієнта бургера, або якщо ви хочете закінчити введіть любе інше число: '))
    try:
        my_burger.burger += [ingredients[user]]
    except IndexError:
        push = True
else:
    print('\n'.join(my_burger.burger))
