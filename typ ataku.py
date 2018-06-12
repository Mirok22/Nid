#Muszę jeszcze wpisać inventarz, żeby można było wybierać broń z inventarza.
# Porównanie ataku z obroną

import random

attack_type = int(input("Podaj typ ataku (od 1 do 10): "))

while attack_type not in range(1, 11):
    print("\nNieprawidłowy typ ataku!\n")
    attack_type = int(input("Podaj typ ataku (od 1 do 10): "))

attack = random.randint(1, 20) + attack_type
offense = random.randint(1, 20)

print("\nSiła ataku", attack)
print("Siła obrony", offense)