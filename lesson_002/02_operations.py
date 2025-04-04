# -*- coding: utf-8 -*-

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "1 2 3" и "9"
# result = (1 + 2) * 3
# print(result)

def main():
    res = (1 * 2 + 3) * 4 + 5
    return res, '(1 * 2 + 3) * 4 + 5'


if __name__ == '__main__':
    res1 = main()
    print(f'Завдання: Расставьте знаки операций "плюс", "минус", "умножение" и скобки '
          f'между числами "1 2 3 4 5" так, что бы получилось число "25". \n '
          f'{res1[-1]} = {res1[0]}')
