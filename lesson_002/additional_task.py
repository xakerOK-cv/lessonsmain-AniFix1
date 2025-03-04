from pprint import pprint
import re


# 1 завдання
def even_numbers(user):
    res = []
    x = 1
    while x <= user:
        x += 1
        if x % 2 == 0:
            res += [x]
    return res


# 2 завдання
def summation(user):
    res = 0
    for i in user:
        if i > 0:
            res += i
    return res


# 3 завдання
def multiplication_table(integer=0):
    res = []
    for i in range(1, 11):
        res.append(f"{i} * {integer} = " + str(i * integer))
    return res


# 4 завдання
# Зроблено завдяки https://surl.li/xfphbt
def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and num % 3 != 0

    for i in range(3, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False

    return prime


def main():
    print(
        "1. Вивести всі парні числа від 1 до n. Користувач вводить число n, і програма повинна надрукувати всі "
        "парні числа в цьому діапазоні.\n"
        "2. Користувач вводить 5 чисел. Програма підраховує та виводить суму тільки додатних чисел.\n"
        "3. Створити програму, яка запитує у користувача число n і виводить таблицю множення для цього числа "
        "від 1 до 10.\n"
        "4. Написати програму, яка перевіряє, чи є введене число простим (ділиться тільки на 1 і на себе).\n"
        "5. Користувач вводить рядок тексту, а програма замінює всі голосні літери (а, е, є, и, і, ї, о, у, ю, я) "
        "на символ *.\n")
    task = int(input("Введіть цифру завдання на яке ви хочете перевірити: "))

    # Це просто, щоб легко вибирати завдання, але прикро, що я не зразу це зробив
    # і мусив попередні завдання коментувати для легкої перевірки поточного.
    if task == 1:
        # 1 завдання
        user_number1 = int(input("Введіть до куда порахувати парні числа: "))
        pprint(even_numbers(user_number1), width=40, compact=True)
    elif task == 2:
        # 2 завдання
        i = 1
        user_number2 = []
        print("\nВведіть числа, які потрібно сумувати, по черзі(дія виконається тільки з додатніми): ")
        while i <= 5:
            user_number2.append(int(input(f"№{i} : ")))
            i += 1
        print(summation(user_number2))
    elif task == 3:
        # 3 завдання
        user_number3 = int(input("Введіть число для, якого потрібно зробити таблицю множення: "))
        pprint(multiplication_table(integer=user_number3), compact=True, width=40)
    elif task == 4:
        # 4 завдання
        user_number4 = int(input("Введіть число, яке потрібно перевірити, чи просте воно: "))
        if is_prime(user_number4):
            pprint(f"Число {user_number4} начебто являється простим.")
        else:
            pprint(f"Число {user_number4} не являється простим.")
    elif task == 5:
        # 5 завдання
        user_text = str(input("Введіть текст в якому потрібно замінити голосні літери: "))
        text = re.sub('[аеєиіїоуюяАЕИІЇОУЮЯ]', '*', user_text)
        pprint(f"Ваш відформатований текст: {text}")
    else:
        print("Ви ввели на правильне число!")


if __name__ == '__main__':
    main()


# нормас) прикольно зробив це можна дати прогу *.exe як учебку для 6 класу
# прикольно.. ти зробив спочатку код потім удосконалював. фукції добавив так?

