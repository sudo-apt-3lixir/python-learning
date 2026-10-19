import random

weapon = False
money = 1000
health = 100
rounds = 0

print("==============================")
print("        CASINO HEIST")
print("==============================")
print("Goal: Get 10 000 kr")
print()

while money < 10000 and health > 0:

    rounds += 1

    print()
    print("------------------------------")
    print("Round:", rounds)
    print("Money:", money, "kr")
    print("Health:", health)
    print("------------------------------")

    print("1. Work")
    print("2. Rob")
    print("3. Gamble")
    print("4. Shop")
    print("5. Stats")
    print("6. Quit")

    choice = input("Choose: ")

    if choice == "1":

        number = random.randint(1, 10)

        print("You chose work")

        if number == 1:
            money += 1000
            print("You gained 1000 money")

        elif number == 2:
            money += 750
            print("You gained 750 money")

        else:
            money += 500
            print("You gained 500 money")

    elif choice == "2":

        print("You chose rob")

        number = random.randint(1, 10)

        if weapon == True:

            if number <= 7:
                money += 2000
                print("The robbery was successful!")
                print("You gained 2000 kr.")

            else:
                health -= 20
                print("You got caught!")
                print("You lost 20 health.")

        else:

            if number <= 4:
                money += 2000
                print("The robbery was successful!")
                print("You gained 2000 kr.")

            else:
                health -= 20
                print("You got caught!")
                print("You lost 20 health.")

    elif choice == "3":
           

        print("You chose gamble")
        print("1. Bet 100 kr")
        print("2. Bet 250 kr")
        print("3. Bet 500 kr")

        bet = input("Choose your bet: ")

        if bet == "1":
            bet_amount = 100

        elif bet == "2":
            bet_amount = 250

        elif bet == "3":
            bet_amount = 500

        else:
            print("Invalid choice!")
            continue

        if money >= bet_amount:

            number = random.randint(1, 2)

            if number == 1:
                money += bet_amount
                print("You won!")
                print("You gained", bet_amount, "kr.")

            else:
                money -= bet_amount
                print("You lost!")
                print("You lost", bet_amount, "kr.")

        else:
            print("You don't have enough money!")
        pass

    elif choice == "4":

        print()
        print("========== SHOP ==========")
        print("1. Medkit - 200 kr")
        print("2. Weapon - 500 kr")
        print("3. Leave shop")

        shop_choice = input("Choose: ")

        if shop_choice == "1":

            if money >= 200:
                money -= 200
                health += 30

                if health > 100:
                    health = 100

                print("You bought a medkit!")

            else:
                print("You don't have enough money!")

        elif shop_choice == "2":

            if weapon == True:
                print("You already have a weapon!")

            elif money >= 500:
                money -= 500
                weapon = True
                print("You bought a weapon!")

            else:
                print("You don't have enough money!")

        elif shop_choice == "3":
            print("You left the shop.")

        else:
            print("Invalid choice!")

    elif choice == "5":

        print()
        print("========== STATS ==========")
        print("Money:", money, "kr")
        print("Health:", health)

        if weapon == True:
            print("Weapon: Yes")
        else:
            print("Weapon: No")

        print("Rounds:", rounds)
        print("===========================")
        pass

    elif choice == "6":
        print("You left the game.")
        break

    else:
        print("Invalid choice!")


if money >= 10000:
    print()
    print("YOU DID IT!")
    print("You escaped with", money, "kr.")

elif money <= 0:
    print()
    print("You lost")
    print("You got captured and couldnt escape with the money")

elif health <= 0:
    print()
    print("GAME OVER!")