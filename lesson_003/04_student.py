# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000


# TODO здесь ваш код
=======
a = 0
n = 9
All_expenses = expenses
print(All_expenses)
while a < n:
    incruese_expense = (expenses * 0.03)
    expenses = expenses + incruese_expense
    All_expenses = All_expenses + expenses
    educational_grant = educational_grant + 10000
    print("Educational_grant: ",educational_grant)
    print("Incruese expense: ",round(incruese_expense))
    print("Expenses: ",round(expenses))
    print("Global expenses: ",round(All_expenses))
    a += 1

All_needs_money = All_expenses - educational_grant
print("Student must asked",round(All_needs_money,2),"money")

