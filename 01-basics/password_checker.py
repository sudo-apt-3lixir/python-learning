import json
print("===== PERSONLIG INFO =====")

name = input("Vad heter du? ")

while True:
    try:
        age = int(input("Hur gammal är du? "))
        break
    except ValueError:
        print("Du måste skriva en siffra!")

while True:
    try:
        height = float(input("Hur lång är du i meter? "))
        break
    except ValueError:
        print("Du måste skriva längden som ett nummer, t.ex. 1.90!")

game = input("Vilket är ditt favoritspel? ")


def show_info():
    print()
    print("===== INFO =====")
    print(f"Namn: {name}")
    print(f"Ålder: {age} år")
    print(f"Längd: {height:.2f} meter")
    print(f"Favoritspel: {game}")

    print()

    if name.lower() == "oliwer":
        print("Välkommen tillbaka, Oliwer!")
    else:
        print(f"Trevligt att träffas, {name}!")

    if height < 1.90:
        print("Jäklar vad du är kort!")
    elif height > 1.90:
        print("Jäklar vad du är lång!")
    else:
        print("Exakt 1.90 meter!")

    game_lower = game.lower()

    if game_lower == "minecraft":
        print("Minecraft är ett bra val!")
    elif game_lower == "cs2":
        print("CS2, nice!")
    else:
        print("Jag känner inte till det spelet!")

    months = age * 12
    print(f"Du har levt ungefär {age} år, eller {months} månader.")


def change_info():
    global name, age, height, game
    
    def save_info():
        data = {
        
        
        "name": name,
        "age": age,
        "height": height,
        "game": game
    }

    with open("info.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Informationen har sparats!")

    while True:
        print()
        print("===== ÄNDRA INFO =====")
        print("1. Namn")
        print("2. Ålder")
        print("3. Längd")
        print("4. Favoritspel")
        print("5. Tillbaka")

        change = input("Vad vill du ändra? ")

        if change == "1":
            name = input("Nytt namn: ")
            print("Namnet har ändrats!")

        elif change == "2":
            while True:
                try:
                    age = int(input("Ny ålder: "))
                    break
                except ValueError:
                    print("Du måste skriva en siffra!")

            print("Åldern har ändrats!")

        elif change == "3":
            while True:
                try:
                    height = float(input("Ny längd i meter: "))
                    break
                except ValueError:
                    print("Du måste skriva ett nummer, t.ex. 1.90!")

            print("Längden har ändrats!")

        elif change == "4":
            game = input("Nytt favoritspel: ")
            print("Favoritspelet har ändrats!")

        elif change == "5":
            break

        else:
            print("Ogiltigt val! Välj 1-5.")


while True:
    print()
    print("===== MENY =====")
    print("1. Visa information")
    print("2. Ändra information")
    print("3. Avsluta")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        show_info()

        print()
        print("1. Öppna menyn")
        print("2. Ändra information")
        print("3. Avsluta")

        info_choice = input("Vad vill du göra? ")

        if info_choice == "1":
            continue

        elif info_choice == "2":
            change_info()

        elif info_choice == "3":
            print("Programmet avslutas...")
            break

        else:
            print("Ogiltigt val!")

    elif choice == "2":
        change_info()

    elif choice == "3":
        print("Programmet avslutas...")
        break

    else:
        print("Ogiltigt val! Välj 1, 2 eller 3.")