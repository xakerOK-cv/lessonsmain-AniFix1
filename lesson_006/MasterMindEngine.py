import random

the_number = ''


def guess_the_number():
    global the_number
    the_number = the_number.join(random.sample('123456789', 4))


def check_the_number(u_number):
    lists = [0, 0]

    for index, number in enumerate(u_number):
        for my_index, my_number in enumerate(the_number):
            if index == my_index and number == my_number:
                lists[1] += 1
            elif number == my_number:
                lists[0] += 1

    return lists
