# Funkcja "menu"

results = [("Alfred", 10), ("Janek", 5), ("Darek", 15)]


def show_menu():

    print("\nMENU:\ntop - wyświetl najlepsze wyniki\ndodaj - dodaj wynik\ngraj - zacznij nową grę")


def sort_results(scores_list):
    names, scores = [], []
    for i in range(len(scores_list)):
        tmp_name, tmp_score = scores_list[i]
        names.append(tmp_name)
        scores.append(tmp_score)

    for i in range(1, len(scores)):
        key_scores = scores[i]
        key_names = names[i]
        j = i - 1
        while j >= 0 and scores[j] > key_scores:
            scores[j + 1] = scores[j]
            names[j + 1] = names[j]
            j = j - 1
        scores[j + 1] = key_scores
        names[j + 1] = key_names

    while results:
        results.pop()

    while names and scores:
        results.append((names.pop(), scores.pop()))


def show_top():
    sort_results(results)
    print("\nNick\tWynik")
    for i in range(len(results)):
        name, score = results[i]
    print("%s\t%s" % (name, score))


def add_result():
    result = input("\nPodaj imię i wynik (oddzielone przecinkiem): ")
    name, score = result.split(",")
    score = int(score)

    results.append((name, score))


def play_game():
    name = input("\nPodaj swoje imię: ")
    score = 0



show_menu()

command = input("\nCo chcesz zrobić? (pusta komenda kończy program) ")

while command:
    if command == "top":
        show_top()
    elif command == "dodaj":
        add_result()
    elif command == "graj":
        play_game()
    else:
        print("\nNieprawidłowa komenda!")

    show_menu()
    command = input("\nCo chcesz zrobić? (pusta komenda kończy program) ")