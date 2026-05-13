# -*- coding: utf-8 -*-
import random


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   Купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу:)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)


class Home:
    def __init__(self):
        self.residents = None
        self.pets = []
        self.food = 0
        self.budget = 0
        self.cleanliness = 100
        self.day = 0

    def add_residents(self, residents):
        self.residents = residents

    def add_pet(self, pet):
        self.pets.append(pet)

    def add_food(self, food):
        self.food += food

    def add_budget(self, budget):
        self.budget += budget


class Creature:
    def __init__(self, home):
        self.satiety = 100
        self.home = home
        self.life = True

    def get_name(self):
        if isinstance(self, Human):
            return 'Людина'

        if isinstance(self, Cat):
            if self in self.home.pets:
                return f'Кіт №{self.home.pets.index(self) + 1}'
            return 'Кіт'

        return 'Істота'

    def log(self, text):
        print(f'[День {self.home.day:03}] {text}')

    def normalize_stats(self):
        self.satiety = max(0, min(self.satiety, 100))
        self.home.cleanliness = max(0, min(self.home.cleanliness, 100))

    def eat(self, portion: int):
        if self.home.food > 0:
            eaten = min(portion, self.home.food)
            satiety_before = self.satiety
            food_before = self.home.food

            self.satiety += eaten * 2
            self.home.food -= eaten
            self.normalize_stats()

            self.log(
                f'{self.get_name()} поїв. '
                f'Їжа: {food_before} -> {self.home.food}. '
                f'Ситість: {satiety_before} -> {self.satiety}.'
            )
            return True

        self.log(f'{self.get_name()} хотів поїсти, але їжі немає.')
        return False

    def action(self, actions: tuple | None = None):
        if actions is None:
            raise Exception('Немає доступних дій')

        if self.satiety < 50:
            if self.home.food > 0:
                self.eat(portion=10 if isinstance(self, Cat) else 15)
                return None

            if isinstance(self, Cat):
                self.log(f'{self.get_name()} голодний, але їжі немає.')

            if isinstance(self, Human):
                if self.buy_food():
                    return None

                self.go_to_work()
                return None

        if isinstance(self, Human) and self.home.food <= 0:
            if self.buy_food():
                return None

            self.go_to_work()
            return None

        if isinstance(self, Human) and self.home.cleanliness < 65:
            self.clean_the_house()
            return None


        ret = actions[random.randint(0, len(actions) - 1)]()

        if ret is not None:
            return ret

        return None

    def life_check(self):
        if self.satiety <= 0 and self.life:
            self.life = False
            self.log(f'{self.get_name()} помер від голоду.')


class Human(Creature):

    def __init__(self, home, settings):
        super().__init__(home)
        self.setting = settings
        self.home.add_residents(self)

    def pic_up_the_cat(self):
        self.log('Людина побачила кота під дверима і підібрала його.')
        cat = Cat(self.home)
        self.home.add_pet(cat)
        return cat

    def buy_food(self):
        if self.home.budget > 0:
            max_affordable_food = self.home.budget // self.setting[0]

            if max_affordable_food == 0:
                self.log(
                    f'Людина хотіла купити їжу, але грошей замало. '
                    f'Гроші: {self.home.budget}.'
                )
                return False

            food_before = self.home.food
            budget_before = self.home.budget

            bought_food = min(max_affordable_food, self.setting[1])
            price = bought_food * self.setting[0]

            self.home.add_food(bought_food)
            self.home.budget -= price

            self.log(
                f'Людина купила їжу. '
                f'Куплено: {bought_food}. '
                f'Їжа: {food_before} -> {self.home.food}. '
                f'Гроші: {budget_before} -> {self.home.budget}.'
            )
            return True

        self.log('Людина хотіла купити їжу, але грошей немає.')
        return False

    def go_to_work(self):
        budget_before = self.home.budget
        self.home.add_budget(150)

        self.log(
            f'Людина пішла на роботу. '
            f'Гроші: {budget_before} -> {self.home.budget}.'
        )

    def clean_the_house(self):
        satiety_before = self.satiety
        cleanliness_before = self.home.cleanliness

        self.home.cleanliness = 100
        self.satiety -= 20
        self.normalize_stats()

        self.log(
            f'Людина прибрала в домі. '
            f'Чистота: {cleanliness_before} -> {self.home.cleanliness}. '
            f'Ситість: {satiety_before} -> {self.satiety}.'
        )

    def game(self):
        satiety_before = self.satiety

        self.satiety -= 20
        self.normalize_stats()

        self.log(
            f'Людина пограла. '
            f'Ситість: {satiety_before} -> {self.satiety}.'
        )


class Cat(Creature):

    def __init__(self, home):
        super().__init__(home)

    def sleep(self):
        satiety_before = self.satiety

        self.satiety -= 10
        self.normalize_stats()

        self.log(
            f'{self.get_name()} поспав. '
            f'Ситість: {satiety_before} -> {self.satiety}.'
        )

    def sharpen_its_claws(self):
        satiety_before = self.satiety
        cleanliness_before = self.home.cleanliness

        self.satiety -= 10
        self.home.cleanliness -= 5
        self.normalize_stats()

        self.log(
            f'{self.get_name()} подер обої. '
            f'Ситість: {satiety_before} -> {self.satiety}. '
            f'Чистота: {cleanliness_before} -> {self.home.cleanliness}.'
        )



def main():
    settings = []
    if 'y' == str(input('Ви хочете налаштувати сесію? Якщо так введіть y. ')):
        settings.append(int(input('Введіть максимальну кількість котів (стандартно 1): ')))
        settings.append(int(input('Введіть ціну за одиницю продукту (стандартно 2): ')))
        settings.append(int(input('Введіть скільки можна купити за раз (стандартно 50): ')))


    home = Home()
    human = Human(home=home, settings=settings[1:] if len(settings) != 0 else [2, 50])
    cats = []

    day = 0

    while day < 365:
        home.day = day + 1
        print(f'\n{'='*10} День {home.day} {'='*10}')
        if human.life :
            max_cats = settings[0] if len(settings) != 0 else 1
            if len(home.pets) < max_cats:
                cat = human.action(actions=(human.go_to_work, human.pic_up_the_cat, human.game))
                if cat is not None:
                    cats.append(cat)
            else:
                human.action(actions=(human.go_to_work, human.game))
        human.life_check()


        if len(cats) > 0 :
            for cat in cats:
                if cat.life :
                    cat.action(actions=(cat.sleep, cat.sharpen_its_claws))
                    cat.life_check()
        alive_cats = sum(1 for cat in cats if cat.life)

        print(
            f'[День {home.day:03}] Підсумок дня: '
            f'людина: {"жива" if human.life else "мертва"}, '
            f'ситість людини: {human.satiety}, '
            f'живих котів: {alive_cats}/{len(cats)}, '
            f'їжа: {home.food}, '
            f'гроші: {home.budget}, '
            f'чистота: {home.cleanliness}.'
        )

        day += 1


if __name__ == '__main__':
    main()