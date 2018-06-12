import random


class Survivor(object):
    """Klasa survivors"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.CONST_ATTACK = 5
        self.is_win = False

    def attack(self, zombie):
        """Metoda ataku"""
        tmp_attack = random.randint(1, 20) + self.CONST_ATTACK
        zombie.defense(tmp_attack)
        print("%s zadał %d obrażeń %s" % (self.name, tmp_attack, zombie.race))

    def defense(self, attack):
        """Metoda obrony"""
        self.hp -= attack


class Zombie(object):
    """Klasa zombie"""

    def __init__(self, race, hp):
        self.race = race
        self.hp = hp
        self.CONST_ATTACK = 5
        self.is_win = False

    def attack(self, zombie):
        """Metoda ataku"""
        tmp_attack = random.randint(1, 20) + self.CONST_ATTACK
        zombie.defense(tmp_attack)
        print("%s zadał %d obrażeń %s" % (self.race, tmp_attack, zombie.name))

    def defense(self, attack):
        """Metoda obrony"""
        self.hp -= attack


survivor = Survivor("Jack", 100)
zomb = Zombie("Zombie", 100)

while survivor.hp > 0 and zomb.hp > 0:
    print("\nDostępne opcje:\n- walka\n- uciekaj\n")
    option = input("> ")

    if option == "walka":
        survivor.attack(zomb)
        if zomb.hp <= 0:
            survivor.is_win = True
            break
    elif option == "uciekaj":
        print("\nUciekasz od zombie!")
        break
    else:
        survivor.attack(zomb)
        if zomb.hp <= 0:
            survivor.is_win = True
            break

    zomb.attack(survivor)
    if survivor.hp <= 0:
        zomb.is_win = True
        break

if survivor.is_win:
    print("\n%s wins!" % survivor.name)
elif zomb.is_win:
    print("\n%s wins!" % zomb.race)
else:
    print("\nObszedłeś walkę!")