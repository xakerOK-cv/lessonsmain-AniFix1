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

def life(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.life:
            return func(self, *args, **kwargs)
        else:
            match type(self).__name__:
                case 'Husband':
                    print(f"{self.name} мертвий.")
                case 'Wife' :
                    print(f"{self.name} мертва.")
                case _ :
                    print(f"{self.name} мертвий.")
            return False
    return wrapper

def normalize_stats(norm):
     norm = max(0, min(norm, 100))
     return norm

class House:

    def __init__(self):
        self.residents = []
        self.pets = []
        self.food = 50
        self.money = 100
        self.mud = 0
        self.log = {'money_yesterday' : 0,
                    'money_for_the_whole_time' : 0,
                    'food_yesterday' : 0,
                    'food_for_the_whole_time' : 0,
                    'mud_yesterday' : 0,
                    'fur_coat_yesterday' : 0,
                    'fur_coat_for_the_whole_time' : 0 }

    def __str__(self):
        print(f'{'='*10}',
              'Сьогодні в будинку:',
              *[f"Жителі: {r.name} ==> {'Живий' if r.life else 'Мертвий'}" for r in self.residents],
              # *[f"Улюбленці: {self.pets.name} ==> "
              #   f"{'Живий' if self.pets.life else 'Мертвий'}" for r in self.residents],
              f"Кошти: {self.log['money_for_the_whole_time']} ==> {self.money}",
              f"Їжі: {self.log['food_yesterday']} ==> {self.food}",
              f"Забрудненість: {self.log['mud_yesterday']} ==> {self.mud}",)
        self.gets_muddied()

    def gets_muddied(self):
        if not self.mud >= 100:
            normal = min(5, 100 - self.mud)
            self.mud += normal

    def add_residents(self, residents):
        self.residents.append(residents)

    def add_pet(self, pet):
        self.pets.append(pet)

    def add_food(self, food):
        self.log['food_yesterday'] = self.food
        self.food += food
        self.log['food_for_the_whole_time'] += food

    def add_money(self, money):
        self.log['money_yesterday'] = self.money
        self.money += money
        self.log['money_for_the_whole_time'] += money


class Human:

    def __init__(self, home, name=''):
        self.life = True
        self.name = name
        self.home = home
        self.satiety = 30
        self.happiness = 100
        self.last_action = ''

    @life
    def __str__(self):
        if self.last_action == 'eat':
            match type(self).__name__:
                case 'Husband':
                    print(f"{self.name} ")
                case 'Wife':
                    print(f"{self.name} ")
                case 'Pet':
                    print(f"{self.name} ")
                case _:
                    raise Exception(f"Невідомий класс {type(self).__name__}, {self.name}.")
        else:
            match self.last_action:
                case 'work':
                    print(f"{self.name} попрацював.")
                case 'gaming':
                    print(f"{self.name} пограв.")
                case 'buy_food':
                    print(f"{self.name} купила їжі.")
                case 'buy_fur_coat':
                    print(f"{self.name} купила шубу.")
                case 'not_buy_fur_coat':
                    print(f"{self.name} не вистачило на шубу.")
                case 'clean_house':
                    print(f"{self.name} віддраяла будинок.")
                case _:
                    raise ValueError(f"Невідома дія: {self.last_action}")
        self.fall_of_happiness()

        self.satiety = normalize_stats(norm=self.satiety)
        self.happiness = normalize_stats(norm=self.happiness)

    def fall_of_happiness(self):
        if 90 < self.home.mud:
            self.happiness -= min(self.happiness, 10)
        elif self.home.mud <= 90:
            self.happiness -= min(self.happiness, 5)

    def loss_of_satiety(self):
        if self.satiety >= 0 :
            self.satiety -= min(self.satiety, 10)
        else:
            self.life = False

    def add_happiness(self, happiness):
        self.happiness += happiness

    def eat(self, portion: int):
        eaten = min(portion, self.home.food)
        self.satiety += eaten * 1
        self.home.add_food(-eaten)
        return 'eat'

    # НІКОЛИ НЕ ПОВЕРТАТИ FALSE
    def action(self, actions: tuple | None = None):
        if actions is None:
            raise Exception('Немає доступних дій')

        if self.satiety < 50:
            if self.home.food > 0:
                self.last_action = self.eat(portion=30)
                return True

            # if isinstance(self, Cat):
            #     self.log(f'{self.get_name()} голодний, але їжі немає.')

        if isinstance(self, Husband) and self.home.money <= 50:
            self.last_action = self.work()
            return True

        more_necessary = True if (self.home.food <= 65 and self.home.money > 0) or self.home.mud >= 60 else False

        if isinstance(self, Wife) and more_necessary:
            if self.home.mud >= 60:
                self.last_action = self.clean_house()
                return True

            if self.home.food <= 65 and self.home.money > 0:
                self.last_action = self.buy_food()
                return True

            raise Exception(f"Помилка в логіці")



        if actions is not None:
            self.last_action = actions[random.randint(0, len(actions) - 1)]()
            return True

        raise Exception(f"Не одна дія не була виконана")


class Husband(Human):

    def __init__(self, home, name=''):
        super().__init__(home=home, name=name)

    def __str__(self):
        return super().__str__()

    def act(self, actions: tuple | None):
        if self.life:
            return super().action(actions=actions)
        return None


    def eat(self,portion):
        return super().eat(portion=portion)

    def work(self):
        self.home.add_money(150)
        self.loss_of_satiety()
        return 'work'

    def gaming(self):
        self.add_happiness(20)
        self.loss_of_satiety()
        return 'gaming'


class Wife(Human):

    def __init__(self, home, name=''):
        super().__init__(home=home, name=name)
        self.fur_coat = 0

    def __str__(self):
        return super().__str__()

    def act(self, actions: tuple | None):
        if self.life:
            return super().action(actions=actions)
        return None

    def eat(self, portion):
        return super().eat(portion=portion)

    def buy_food(self):
        food_to_buy = min(self.home.money, 50)
        self.home.add_food(food_to_buy)
        self.home.money -= food_to_buy
        self.loss_of_satiety()
        return 'buy_food'

    def buy_fur_coat(self):
        if self.home.money >= 350:
            self.home.log['fur_coat_yesterday'] = self.home.fur_coat
            self.fur_coat += 1
            self.home.log['fur_coat_for_the_whole_time'] += 1
            self.home.money -= 350
            self.add_happiness(60)
            self.loss_of_satiety()
            return 'buy_fur_coat'
        else:
            return 'not_buy_fur_coat'

    def clean_house(self):
        self.home.mud = 100
        self.loss_of_satiety()
        return 'clean_house'


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

cprint(f"Прожито днів {day + 1}, зароблено грошей {home.log['money_for_the_whole_time']}, "
       f"куплено шуб {home.log['fur_coat_for_the_whole_time']}, з'їдено їжі {home.log['food_for_the_whole_time']}",
       colors='green')
       



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












# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


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

