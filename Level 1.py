Poziom1 = {
    1: {"name": "lokacje1",
        "east": 2,
        "south": 3},
    2: {"name": "lokacje2",
        "west": 1,
        "south": 4},
    3: {"name": "lokacje3",
        "north": 1},
    4: {"name": "Bathroom",
        "north": 2}
}

currentRoom = 1
print("Use command:")
print("> go [direction]")
print("> exit")
print("Command:")

while True:
    print("You are in " + rooms[currentRoom]["name"])
    move = input("> ").lower().split()
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")
    if move[0] == "exit":
        print("You exit the game!")
        break