#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> грн

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
# tables
table_code = goods['Стол']
tables_item = store[table_code][0]
tables_item2 = store[table_code][1]
tables_quantity = tables_item['quantity']
tables_quantity2 = tables_item2['quantity']
All_tables_quantity = tables_quantity + tables_quantity2
tables_price = tables_item['price']
tables_price2 = tables_item2['price']
tables_cost = tables_quantity * tables_price
tables_cost2 = tables_quantity2 * tables_price2
All_tables_cost = tables_cost + tables_cost2
print('Tables = ',All_tables_quantity,',price',All_tables_cost,'rub')
#sofas

sofa_code = goods['Диван']
sofas_item = store[sofa_code][0]
sofas_item2 = store[sofa_code][1]
sofas_quantity = sofas_item['quantity']
sofas_quantity2 = sofas_item2['quantity']
All_sofas_quantity = sofas_quantity + sofas_quantity2
sofas_price = sofas_item['price']
sofas_price2 = sofas_item2['price']
sofas_cost = sofas_quantity * sofas_price
sofas_cost2 = sofas_quantity2 * sofas_price2
All_sofas_cost = sofas_cost + sofas_cost2
print('Sofas = ',All_sofas_quantity,',price',All_sofas_cost,'rub')

# chairs
chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_item2 = store[chair_code][1]
chairs_item3 = store[chair_code][2]
chairs_quantity = chairs_item['quantity']
chairs_quantity2 = chairs_item2['quantity']
chairs_quantity3 = chairs_item3['quantity']
All_chairs_quantity = chairs_quantity + chairs_quantity2 + chairs_quantity3
chairs_price = chairs_item['price']
chairs_price2 = chairs_item2['price']
chairs_price3 = chairs_item3['price']
chairs_cost = chairs_quantity * chairs_price
chairs_cost2 = chairs_quantity2 * chairs_price2
chairs_cost3 = chairs_quantity3 * chairs_price3
All_chairs_cost = chairs_cost + chairs_cost2 + chairs_cost3
print('Chairs = ',All_chairs_quantity,',price',All_chairs_cost,'rub')




$ ВСЕ СУПЕР ВИДНО ПОРАБОТАЛ) 





