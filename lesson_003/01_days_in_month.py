# -*- coding: utf-8 -*-


# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# user_input = input("Введите, пожалуйста, номер месяца: ")
# month = int(user_input)
# print('Вы ввели', month)

def main():
    months = [
        31, 28, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31
    ]
    input_user = input("Введіть, будь-ласка, номер місяцю: ")
    if input_user.isdigit():
        month = int(input_user)

        if 12 >= month > 0:
            print(f'Ви ввели {month} місяць, в ньому {months[month - 1]} днів.')

        else:
            print('Ви ввели не існуючи номер місяця\n')
            main()
    else:
        print('Ви ввели не коректну дату, введіть будь-ласка, номер цифрою\n')
        main()


if __name__ == '__main__':
    main()

# завдання просте, але сроблено класично що правильно
