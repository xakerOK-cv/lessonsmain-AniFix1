#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

element = ','

# Тут я буду перебирати текст в пошуках коми та відштовхуючись
# від них нарізати увесь текст на назви фільмів(по факту костиль .split())

def cutting(elements, txt):
    # Об'явлення списків
    locations = []
    res = []
    slise = [0, 1]
    # Пошук ком в тексті
    for index, char in enumerate(txt) :
        if char == elements :
            locations.append(index)
    # Перепись першого фільму в списку
    res.append(txt[:locations[0]])
    # Переписування всіх інших фільмів
    for index, index_txt in enumerate(locations) :
        if not len(locations) - 1 == index:
            res.append(txt[locations[slise[0]] + 2:locations[slise[1]]])
            slise[0] = slise[0] + 1
            slise[-1] = slise[1] + 1
        else:
            res.append(txt[locations[-1] + 2:])
    return res

def main():
    data = cutting(element, my_favorite_movies)
    print(f'\nМої улюблені фільми: {my_favorite_movies}'
          f'\nПервий: {data[0]}'
          f'\nПоследний: {data[-1]}'
          f'\nВторой: {data[1]}'
          f'\nВторой с конца: {data[-2]}')

if __name__ == '__main__' :
    main()
