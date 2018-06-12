print("\tWitaj w grze 'Zombie survival'!")
print("\nMożna rabować, budować, walczyć, zajmować się rzemiosłem, gospodarstwem i wędkowania w walce o przetrwanie.")
print("Spróbuj poprawić swoje umiejętności przetrwania i dasz radę przetrwać.\n")

password = input("Wprowadź hasło: ")
if password == "zombie":
    print("Dostęp został udzielony")
else:
    print("Nie masz uprawnień do tego zasobu, sprobuj ponownie")

inventory = ["pistolet TT", "plecak (small)", "nóż", "bandaż(x1)","puszka 'Coca-Cola'(x1)","baton czekoladowy (x1)"]
portfel = ["65$", "karta'PKO'", "klucz(?)"]
print("Znajdujesz w plecaku zamordowanego, który zawiera:")
print (portfel)
print ("Dodajesz zawartość portfela do swojego inwentarza.")
inventory += portfel
print("Twój aktualny inwentarz to:")
print(inventory)