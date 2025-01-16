#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль. (буду знати)
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

def songs_list(data, imp_data):
    res = 0
    for i in imp_data :
        for lists in data:
            if lists[0] == i :
                res = res + lists[-1]
    # Я б не робив округлення якщо тут не видавало .93000000001 чи щось таке не пам'ятаю.
    return round(res, 2)

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

def songs_dict(data, imp_data):
    res = 0
    for i in imp_data :
        for dicts in data:
            if dicts[0] == i :
                res = res + dicts[-1]
    return round(res, 2)


def main():
    sum_time_song1 = songs_list(violator_songs_list,
                                imp_data=['Halo', 'Enjoy the Silence', 'Clean'])
    sum_time_song2 = songs_dict(violator_songs_list,
                                imp_data=['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])

    print(f'Три песни звучат {sum_time_song1} минут')
    print(f'А другие три песни звучат {sum_time_song2} минут')

if __name__ == '__main__' :
    main()