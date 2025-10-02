# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

burger = []

d_cheeseburger = ['Булка', 'Помідор', 'Котлета','Сир', 'Котлета', 'Сир', 'Помідор', 'Огірок', 'Майонез', 'Булка']

def loaf():
    print('А тепер добавимо булку')
    burger.append('Булка')
    return None

def cutlet():
    print('А тепер добавимо котлету')
    burger.append('Котлета')
    return None

def cucumber():
    print('А тепер добавимо огірок')
    burger.append('Огірок')
    return None

def tomato():
    print('А тепер добавимо помідор')
    burger.append('Помідор')
    return None

def mayonnaise():
    print('А тепер добавимо майонез')
    burger.append('Майонез')
    return None

def cheese():
    print('А тепер добавимо сир')
    burger.append('Сир')
    return None

def double_cheeseburger():
    print('\n'.join(d_cheeseburger))
    return None

# Типу чорнетка)