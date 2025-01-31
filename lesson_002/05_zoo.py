#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]


# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
def write(data):
    zoo.insert(1, data)
    return None


# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]


#  и выведите список на консоль
def extension(data):
    zoo.extend(data)
    return None


# уберите слона (elephant)
#  и выведите список на консоль
def remove(data):
    zoo.remove(data)
    return None


# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
def cage(data):
    res = zoo.index(data)
    return res


def out():
    res = ''
    for index, x in enumerate(zoo):
        if index == len(zoo) - 1:
            res = res + zoo[index] + '.'
        else:
            res = res + zoo[index] + ', '
    return res


def main():
    # Перший варіант кода. Але мені не сподобалося, як воно виводить списки(не гарно).

    # write(data='bear')
    # print(zoo)
    # extension(data=birds)
    # print(zoo)
    # remove(data='elephant')
    # print(zoo)
    # print(f'Лев сидить в {cage('lion') + 1} клітці, а'
    #       f' жаворонок в {cage('lark') + 1} клітці.')

    write(data='bear')
    print(out())
    extension(data=birds)
    print(out())
    remove(data='elephant')
    print(out())
    print(f'Лев сидить в {cage('lion') + 1} клітці, а'
          f' жаворонок в {cage('lark') + 1} клітці.')


if __name__ == '__main__':
    main()
