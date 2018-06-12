inventory = ["pistolet TT", "plecak (small)", "nóż", "bandaż(x1)","puszka 'Coca-Cola'(x1)","baton czekoladowy (x1)"]

walka = input("? Zaczynasz walkę:")
if walka == "tak":
    print("Zacząłeś walkę, "+"wybierz sobie broń z inwentarza:")
elif input(inventory) == " ":
    print()
elif walka == "nie":
    print("Ominąłeś walkę,kontynuuj grę.")
