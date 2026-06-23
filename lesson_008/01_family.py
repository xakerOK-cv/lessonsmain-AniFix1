# -*- coding: utf-8 -*-
import random
from functools import wraps

from termcolor import cprint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

def logging(func):
    @wraps(func)
    def info_to_logs(*args, **kwargs):
        pass
        #TODO
    return info_to_logs


class House:

    def __init__(self):
        self.residents = []
        self.pets = []
        self.food = 50
        self.money = 100
        self.mud = 0

    def __str__(self):
        self.gets_muddied()

    def gets_muddied(self):
        if not self.mud >= 100:
            self.mud += 5

    def add_residents(self, residents):
        self.residents.append(residents)

    def add_pet(self, pet):
        self.pets.append(pet)

    def add_food(self, food):
        self.food += food

    def add_money(self, money):
        self.money += money


class Human:

    def __init__(self, home, name=''):
        self.life = True 
        self.name = name
        self.home = home
        self.satiety = 30
        self.happiness = 100

    def __str__(self):
        self.normalize_stats()

    def fall_of_happiness(self):
        if self.life:
            if 90 < self.home.mud:
                self.happiness -= min(self.happiness, 10)
            elif self.home.mud <= 90:
                self.happiness -= min(self.happiness, 5)
                
            return True
        else:
            return False


    def normalize_stats(self):
        self.satiety = max(0, min(self.satiety, 100))
        self.home.mud = max(0, min(self.home.mud, 100))

    def eat(self, portion: int):
        if self.home.food > 0:

            eaten = min(portion, self.home.food)
            self.satiety += eaten * 1
            self.home.add_food(-eaten)

            return True

    def action(self, actions: tuple | None = None):
        if actions is None:
            raise Exception('Немає доступних дій')

        if self.satiety < 50:
            if self.home.food > 0:
                self.eat(portion=10 if isinstance(self, Cat) else 15)
                return None

            # if isinstance(self, Cat):
            #     self.log(f'{self.get_name()} голодний, але їжі немає.')

        if isinstance(self, Husband) and self.home.money <= 50:
            self.work()
            return None

        more_necessary = min(self.home.mud, self.home.food)
        if isinstance(self, Wife) and more_necessary < 65:
            if self.home.mud < 65:
                self.clean_house()
                return None

            if self.home.food < 65:
                self.buy_food()
                return None

            return None



        if actions is not None:
            ret = actions[random.randint(0, len(actions) - 1)]()
            return ret

        return None


class Husband(Human):

    def __init__(self, home, name=''):
        super().__init__(home=home, name=name)

    def __str__(self):
        return super().__str__()

    def act(self, actions: tuple | None):
        super().action(actions=actions)

    def eat(self,portion):
        super().eat(portion=portion)

    def work(self):
        self.home.add_money(150)

    def gaming(self):
        if self.home.mud < 90:
            pass
            #TODO


class Wife(Human):

    def __init__(self, home, name=''):
        super().__init__(home=home, name=name)
        self.fur_coat = 0

    def __str__(self):
        return super().__str__()

    def act(self, actions: tuple | None):
        super().action(actions=actions)

    def eat(self, portion):
        super().eat(portion=portion)

    def buy_food(self):
        pass
    #TODO

    def buy_fur_coat(self):
        if self.home.money >= 350:
            self.fur_coat += 1
            self.home.money -= 350
            return True
        else:
            return False

    def clean_house(self):
        self.home.mud = 100


home = House()
serge = Husband(home=home, name='Сережа')
masha = Wife(home=home, name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act(actions=(serge.gaming, serge.work))
    masha.act(actions=(masha.buy_fur_coat, masha.clean_house, masha.buy_food))
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')



######################################################## Часть вторая
#
# После начать добавлять котов в модель семьи
#

# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass












home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

