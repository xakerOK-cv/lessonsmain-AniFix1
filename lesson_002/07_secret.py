#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]


# ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Требуется задать конкретные индексы, например secret_message[3][12:23:4]
# Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

def decoding(ciphers, keys):
    res = ''
    for index, cipher in enumerate(ciphers):
        fake_res = None
        if isinstance(keys[index], list):
            try:
                if keys[index][2] == 2:
                    res = res + cipher[slice(keys[index][0] - 1, keys[index][1], keys[index][-1])] + ' '
                elif keys[index][2] == -1:
                    fake_res = cipher[slice(keys[index][0] - 1, keys[index][1])]
                    res = res + fake_res[::-1] + ' '
            except IndexError:
                res = res + cipher[slice(keys[index][0] - 1, keys[index][1])] + ' '
        else:
            res = res + cipher[keys[0] - 1] + ' '
    return res[slice(0, -1)]


def main():
    keys = {0: 4, 1: [10, 13], 2: [6, 15, 2],
            3: [8, 13, -1], 4: [17, 21, -1]
            }
    deciphering = decoding(secret_message, keys)
    print(deciphering)


if __name__ == '__main__':
    main()
