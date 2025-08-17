# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
=======

a = 0
user_input = int(input("Введите, пожалуйста, номер месяца: "))
month = int(user_input)
print('Вы ввели', month)

th_0 = '30'
th_1 = '31'
lol = '28(29)'
if month == 1:
    print('He has', th_1, 'days')
elif month == 2:
    print('He has', lol, 'days')
elif month == 3:
    print('He has', th_1, 'days')
elif month == 4:
    print('He has', th_0, 'days')
elif month == 5:
    print('He has', th_1, 'days')
elif month == 6:
    print('He has', th_0, 'days')
elif month == 7:
    print('He has', th_1, 'days')
elif month == 8:
    print('He has', th_1, 'days')
elif month == 9:
    print('He has', th_0, 'days')
elif month == 10:
    print('He has', th_1, 'days')
elif month == 11:
    print('He has', th_0, 'days')
elif month == 12:
    print('He has', th_1, 'days')
else:
    print("Month's number uncorrect")

