# Funkcja postaci
import random


class Postać:

    postać = {}

    @staticmethod
    def create_postać():
        name = input("Podaj imię swojej postaci: ")

        Postać.postać["name"] = name

        points = random.randint(50,100)

        cechy = {
            "siła": 0,
            "odwaga": 0,
            "zręczność": 0,
            "konfliktowość": 0,
            "inteligencja": 0,
            "charyzma": 0,
            "emocjonalność": 0,
            "uczciwość": 0,
            "towarzyskość": 0,
            "umiejętności": 0,
        }

        Postać.postać["cechy"] = {}

        for key in cechy:
            Postać.postać["cechy"][key] = 0
            Postać.postać["cechy"][key] += 5
            points -= 5

        while points:

            print("\nStatystyki:\n")
            for key in cechy:
                print("%s: %d" % (key, Postać.postać["cechy"][key]))

            print("\nPozostałe punkty: %d" % points)

            tmp_cecha = input("Która cecha? ").lower()

            if tmp_cecha in cechy:
                if Postać.postać["cechy"][tmp_cecha] < 20:
                    Postać.postać["cechy"][tmp_cecha] += 1
                else:
                    print("\nCecha '%s' osiągnęła limit!\n" % tmp_cecha)
                    continue
            else:
                print("\nNie ma takiej cechy!\n")
                continue

            points -= 1


postać = Postać
postać.create_postać()

print("\n%s" % postać.postać["name"])

for key in postać.postać["cechy"]:
    print("%s: %d" % (key, postać.postać["cechy"][key]))