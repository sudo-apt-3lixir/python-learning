
import json
import os

FILE_NAME = "people.json"


# =========================
# LADDA PERSONER
# =========================

def load_people():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {}


# =========================
# SPARA PERSONER
# =========================

def save_people():
    with open(FILE_NAME, "w") as file:
        json.dump(people, file, indent=4)

    print("Informationen har sparats!")


# =========================
# LÄGG TILL PERSON
# =========================

def add_person():
    print()
    print("===== LÄGG TILL PERSON =====")

    name = input("Namn: ")

    if name in people:
        print("Den personen finns redan!")
        return

    while True:
        try:
            age = int(input("Ålder: "))
            break
        except ValueError:
            print("Du måste skriva en siffra!")

    while True:
        try:
            height = float(input("Längd i meter: "))
            break
        except ValueError:
            print("Du måste skriva ett nummer, t.ex. 1.90!")

    game = input("Favoritspel: ")

    people[name] = {
        "age": age,
        "height": height,
        "game": game
    }

    print(f"{name} har lagts till!")


# =========================
# VISA EN PERSON
# =========================

def show_person():
    if not people:
        print("Det finns inga personer sparade!")
        return

    print()
    print("===== PERSONER =====")

    names = list(people.keys())

    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    print("0. Tillbaka")

    choice = input("Välj person: ")

    if choice == "0":
        return

    try:
        number = int(choice)
        name = names[number - 1]
    except (ValueError, IndexError):
        print("Ogiltigt val!")
        return

    person = people[name]

    print()
    print("===== INFO =====")
    print(f"Namn: {name}")
    print(f"Ålder: {person['age']} år")
    print(f"Längd: {person['height']:.2f} meter")
    print(f"Favoritspel: {person['game']}")

    print()

    if person["height"] < 1.90:
        print("Jäklar vad du är kort!")
    elif person["height"] > 1.90:
        print("Jäklar vad du är lång!")
    else:
        print("Exakt 1.90 meter!")

    months = person["age"] * 12

    print(
        f"Du har levt ungefär {person['age']} år, "
        f"eller {months} månader."
    )


# =========================
# VISA ALLA PERSONER
# =========================

def show_all():
    if not people:
        print("Det finns inga personer sparade!")
        return

    print()
    print("===== ALLA PERSONER =====")

    for name, person in people.items():
        print()
        print(f"Namn: {name}")
        print(f"Ålder: {person['age']} år")
        print(f"Längd: {person['height']:.2f} meter")
        print(f"Favoritspel: {person['game']}")


# =========================
# ÄNDRA PERSON
# =========================

def edit_person():
    if not people:
        print("Det finns inga personer sparade!")
        return

    print()
    print("===== ÄNDRA PERSON =====")

    names = list(people.keys())

    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    print("0. Tillbaka")

    choice = input("Välj person: ")

    if choice == "0":
        return

    try:
        number = int(choice)
        name = names[number - 1]
    except (ValueError, IndexError):
        print("Ogiltigt val!")
        return

    while True:
        print()
        print(f"===== ÄNDRA {name.upper()} =====")
        print("1. Namn")
        print("2. Ålder")
        print("3. Längd")
        print("4. Favoritspel")
        print("5. Tillbaka")

        choice = input("Vad vill du ändra? ")

        if choice == "1":
            new_name = input("Nytt namn: ")

            if new_name in people:
                print("Det namnet finns redan!")
            else:
                people[new_name] = people.pop(name)
                name = new_name
                print("Namnet har ändrats!")

        elif choice == "2":
            while True:
                try:
                    people[name]["age"] = int(input("Ny ålder: "))
                    break
                except ValueError:
                    print("Du måste skriva en siffra!")

            print("Åldern har ändrats!")

        elif choice == "3":
            while True:
                try:
                    people[name]["height"] = float(
                        input("Ny längd i meter: ")
                    )
                    break
                except ValueError:
                    print("Du måste skriva ett nummer, t.ex. 1.90!")

            print("Längden har ändrats!")

        elif choice == "4":
            people[name]["game"] = input("Nytt favoritspel: ")
            print("Favoritspelet har ändrats!")

        elif choice == "5":
            break

        else:
            print("Ogiltigt val! Välj 1-5.")


# =========================
# TA BORT PERSON
# =========================

def delete_person():
    if not people:
        print("Det finns inga personer sparade!")
        return

    print()
    print("===== TA BORT PERSON =====")

    names = list(people.keys())

    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    print("0. Tillbaka")

    choice = input("Välj person: ")

    if choice == "0":
        return

    try:
        number = int(choice)
        name = names[number - 1]
    except (ValueError, IndexError):
        print("Ogiltigt val!")
        return

    confirm = input(
        f"Är du säker på att du vill ta bort {name}? (j/n): "
    )

    if confirm.lower() == "j":
        del people[name]
        print(f"{name} har tagits bort!")
    else:
        print("Personen har inte tagits bort.")


# =========================
# STATISTIK
# =========================

def show_statistics():
    if not people:
        print("Det finns inga personer att räkna statistik på!")
        return

    ages = []
    heights = []

    for person in people.values():
        ages.append(person["age"])
        heights.append(person["height"])

    average_age = sum(ages) / len(ages)
    average_height = sum(heights) / len(heights)

    oldest_name = max(people, key=lambda name: people[name]["age"])
    youngest_name = min(people, key=lambda name: people[name]["age"])

    tallest_name = max(
        people,
        key=lambda name: people[name]["height"]
    )

    shortest_name = min(
        people,
        key=lambda name: people[name]["height"]
    )

    games = {}

    for person in people.values():
        game = person["game"]

        if game in games:
            games[game] += 1
        else:
            games[game] = 1

    most_common_game = max(games, key=games.get)

    print()
    print("===== STATISTIK =====")
    print(f"Antal personer: {len(people)}")
    print(f"Genomsnittlig ålder: {average_age:.1f} år")
    print(f"Genomsnittlig längd: {average_height:.2f} meter")

    print()
    print(
        f"Äldst: {oldest_name} "
        f"({people[oldest_name]['age']} år)"
    )

    print(
        f"Yngst: {youngest_name} "
        f"({people[youngest_name]['age']} år)"
    )

    print(
        f"Längst: {tallest_name} "
        f"({people[tallest_name]['height']:.2f} meter)"
    )

    print(
        f"Kortast: {shortest_name} "
        f"({people[shortest_name]['height']:.2f} meter)"
    )

    print(
        f"Vanligaste favoritspel: {most_common_game} "
        f"({games[most_common_game]} personer)"
    )


# =========================
# HUVUDPROGRAM
# =========================

people = load_people()

while True:
    print()
    print("===== PERSONDATABAS =====")
    print("1. Lägg till person")
    print("2. Visa person")
    print("3. Visa alla personer")
    print("4. Ändra person")
    print("5. Ta bort person")
    print("6. Statistik")
    print("7. Spara")
    print("8. Avsluta")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        add_person()

    elif choice == "2":
        show_person()

    elif choice == "3":
        show_all()

    elif choice == "4":
        edit_person()

    elif choice == "5":
        delete_person()

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        save_people()

    elif choice == "8":
        save_people()
        print("Programmet avslutas...")
        break

    else:
        print("Ogiltigt val! Välj 1-8.")
