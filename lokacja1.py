lokacje= {
    1: {"name": "Las",
        "wschód": 2,
        "południe": 3,
        "zachód": 5},
    2: {"name": "Miasto",
        "zachód": 1,
        "południe": 4},
    3: {"name": "Góry",
        "północ": 1},
    4: {"name": "Baza wosjkowa",
        "północ": 2},
    5: {"name": "Safe Zone",
        "zachód": 1}
}

currentRoom = 1
print("Użyj komendy:")
print("> go [kierunek]")
print("> exit")
print("Command:")

while True:
    print("Jesteś w lokacji " + lokacje[currentRoom]["name"])
    move = input("> ").lower().split()
    if move[0] == "go":
        if move[1] in lokacje[currentRoom]:
            currentRoom = lokacje[currentRoom][move[1]]
        else:
            print("Nie możesz tam iść!")
    if move[0] == "exit":
        print("Wychodzisz z gry!")
        break