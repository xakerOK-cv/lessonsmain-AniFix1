#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Мама', 'Тато', 'Дід', 'Баба',]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    # Не хочу писати чиїсь імена
    ['Мама', 165],
    ['Тато', 175],
    ['Дід', 170],
    ['Баба', 163],
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

def main() :
    summed = 0
    print(f'Рост отца - {my_family_height[1][1]} см')
    # Не зрозумів общий це сумма чи середнє арифметичне?
    for i in my_family_height :
        summed = summed + i[-1]
    print(f'Общий рост моей семьи - {summed} см')
if __name__ == '__main__' :
    main()