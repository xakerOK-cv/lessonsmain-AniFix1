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

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> грн

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# ↑↑↑↑ Вот це справжня підстава ↑↑↑↑

def main():
    product1 = ['Лампа', store[goods['Лампа']][0]['quantity'],
                store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']]

    product2 = ['Стол', store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity'],
                store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] +
                store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']]

    product3 = ['Диван', store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity'],
                store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] +
                store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']]

    product4 = ['Стул', store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] +
                store[goods['Стул']][2]['quantity'],
                store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] +
                store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] +
                store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']]

    print(f'{product1[0]} - {product1[1]} шт, стоимость {product1[2]} грн (Ціна за увесь товар)')
    print(f'{product2[0]} - {product2[1]} шт, стоимость {product2[2]} грн (Ціна за увесь товар)')
    print(f'{product3[0]} - {product3[1]} шт, стоимость {product3[2]} грн (Ціна за увесь товар)')
    print(f'{product4[0]} - {product4[1]} шт, стоимость {product4[2]} грн (Ціна за увесь товар)')


if __name__ == '__main__' :
    main()






