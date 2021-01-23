#В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.hp = 100
        self.agility = 1
        self.intelligence = 1
        self.strength = 1
        self.base_skill = 1

        @property
        def agilityinc(self):
            return self.agility

        @property
        def intelligenceinc(self):
            return self.intelligence

        @property
        def strengthinc(self):
            return self.strength

    def __repr__(self):
        return f"Name: {self.name}, clan: {self.clan}, agility: {self.agility}, intelligence: {self.intelligence}, strength: {self.strength}"


    def healing(self):
        if (self.hp <= 90) and (self.hp > 0):
            self.hp += 10
        elif (self.hp < 100) and (self.hp > 90):
            self.hp = 100
        elif self.hp > 100:
            self.hp = 100
        elif self.hp <= 0:
            print("you can't heal yourself, you are dead!")

    def increase_base_skill(self):
        if (self.base_skill < 10) and (self.base_skill > 0):
            self.base_skill += 1
        elif self.base_skill > 10:
            self.base_skill = 10
        elif self.base_skill <= 0:
            self.base_skill = 1

class Mage(Unit):
    def __init__(self, name, clan, type_magic):
        super().__init__(name, clan)
        self.type_magic = type_magic

    def __str__(self):
        return f"Unit Class Mage with name {self.name} and Clan {self.clan}"


class Knight(Unit):
    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon

    def __str__(self):
        return f"Unit Class Knight with name {self.name} and Clan {self.clan}"



class Archer(Unit):
    def __init__(self, name, clan, type_bow):
        super().__init__(name, clan)
        self.type_bow = type_bow

    def __str__(self):
        return f"Unit Class Archer with name {self.name} and Clan {self.clan}"

    @property
    def agilityinc(self):
        return self.base_skill



testS = Archer("Stasya", "superclan", "gggg")
print(testS.agility, testS.strength, testS.intelligence)
testS.increase_base_skill()

print(testS.agility, testS.strength, testS.intelligence)