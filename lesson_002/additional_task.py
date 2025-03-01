import pprint
from weakref import finalize


# 1 завдання
def even_numbers(user):
    res = []
    x = 1
    while x <= user :
        x += 1
        if x % 2 == 0 :
            res += [x]
    return res

# 2 завдання
def summation(user):
    res = 0
    for i in user :
        if i > 0 :
            res += i
    return res


def main():
    # 1 завдання
    user_number1 = int(input("Введіть до куда порахувати парні числа: "))
    pprint.pprint(even_numbers(user_number1), width=40, compact=True)

    # 2 завдання
    i = 1
    user_number2 = []
    print("\nВведіть числа, які потрібно сумувати, по черзі(дія виконається тільки з додатніми): ")
    while i <= 5 :
        user_number2.append(int(input(f"№{i} : ")))
        i += 1
    print(summation(user_number2))

    # todo 3. Створити програму, яка запитує у користувача число n і виводить таблицю множення для цього числа від 1 до 10.

    # todo 4. Написати програму, яка перевіряє, чи є введене число простим (ділиться тільки на 1 і на себе).

    # todo 5. Користувач вводить рядок тексту, а програма замінює всі голосні літери (а, е, є, и, і, ї, о, у, ю, я) на символ '*'.



if __name__ == '__main__':
    main()

