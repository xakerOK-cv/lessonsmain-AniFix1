# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
inflation_rate, period = 3, 10


def price_inflation(funds, inflation, duration):
    inflation = inflation / 100 + 1
    duration, res = duration - 1, funds
    while duration > 0:
        duration -= 1
        funds *= inflation
        res += funds
    return res


def remaining(funds, total_costs, duration):
    res = (funds * duration) - total_costs
    return res


def main():
    need_funds = price_inflation(expenses, inflation_rate, period)
    arrears = round(remaining(educational_grant, need_funds, period), 2)
    if arrears >= 0:
        arrears = 0
    else:
        arrears = abs(arrears)
    print(f'Студенту потрібно попросити {arrears} рублів')
    return


if __name__ == '__main__':
    main()


# тут ОК просто математика, але по циклам