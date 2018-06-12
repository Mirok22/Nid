import random

class Postać(object):
    """Klasa bohatera"""
    def __init__(self,hp=100):
        self.hp=hp

    def heal(self):
        self.hp+=random.randint(1,8)
        if self.hp>100:
            self.hp=100
        print("Lekko się uleczyłeś, bohaterze!")

    def walcz(self,wróg):
        self.damage = 5 + random.randint(1,20)
        wróg.obrona(self.damage)

    def obrona (self,damage):
        print("Ała!")
        self.hp=self.hp-damage
        print("Pozostałe hp:",self.hp)

class Wróg(Postać):
    """Klasa przeciwnika"""
    def heal(self):
        self.hp+=random.randint(1,8)
        if self.hp>50:
            self.hp=50
        print("Lekko się uleczyłeś!")
    def character(self):
        wybor = ("dobry", "zły")
        jaki = random.choice(wybor)
        return jaki



def walka(postać, wróg):
    while postać.hp>0 and wróg.hp>0:
        if wróg.character() == "dobry":
            pass
        elif wróg.character() == "zły":
            print("Uciekamy czym prędzej przyjacielu!")
            break
        postać.heal()
        wróg.heal()
        postać.walcz(wróg)
        if wróg.hp<0:
            break
        wróg.walcz(postać)

    if postać.hp > 0:
        print("Zwyciężył bohater!")
        print("Pozostałe hp bohatera:",postać.hp)
    else:
        print("Znowu w życiu Ci nie wyszło")
        print("Pozostałe hp przeciwnika:",wróg.hp)

#main
postać=Postać()
wróg=Wróg(50)
walka(postać,wróg)