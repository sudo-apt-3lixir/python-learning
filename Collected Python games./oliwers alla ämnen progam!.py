
import random

while True:
    print()
    print("===== HUVUDMENY =====")
    print("1. Kalkylator")
    print("2. Lekar")
    print("3. Historia Arcade")
    print("4. Elteknik")
    print("5. Dator och kommunikationsteknik")
    print("6. Programmering")
    print("7. Engelska")
    print("8. Idrott")
    print("9. Hejdå")

    main_choice = input("Välj ett alternativ: ")

    # =========================================================
    # KALKYLATOR
    # =========================================================

    if main_choice == "1":

        while True:
            print()
            print("===== KALKYLATOR =====")
            print("1. Addition")
            print("2. Subtraktion")
            print("3. Multiplikation")
            print("4. Division")
            print("5. Tillbaka till huvudmenyn")

            choice = input("Välj ett alternativ: ")

            if choice == "1":
                number1 = float(input("Skriv tal 1: "))
                number2 = float(input("Skriv tal 2: "))
                print("Svar:", number1 + number2)

            elif choice == "2":
                number1 = float(input("Skriv tal 1: "))
                number2 = float(input("Skriv tal 2: "))
                print("Svar:", number1 - number2)

            elif choice == "3":
                number1 = float(input("Skriv tal 1: "))
                number2 = float(input("Skriv tal 2: "))
                print("Svar:", number1 * number2)

            elif choice == "4":
                number1 = float(input("Skriv tal 1: "))
                number2 = float(input("Skriv tal 2: "))

                if number2 == 0:
                    print("Du kan inte dela med 0!")
                else:
                    print("Svar:", number1 / number2)

            elif choice == "5":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # LEKAR
    # =========================================================

    elif main_choice == "2":

        while True:
            print()
            print("===== LEKAR =====")
            print("1. Gissa numret")
            print("2. Sant eller falskt")
            print("3. Matte tävling")
            print("4. Tillbaka till huvudmenyn")

            game_choice = input("Välj ett spel: ")

            if game_choice == "1":
                print()
                print("===== GISSA TALET =====")
                print("Jag tänker på ett tal mellan 1 och 100!")

                nummer = random.randint(1, 100)
                försök = 0

                while True:
                    gissning = int(input("Gissa talet: "))
                    försök += 1

                    if gissning < nummer:
                        print("För lågt!")

                    elif gissning > nummer:
                        print("För högt!")

                    else:
                        print("Rätt! 🎉")
                        print("Du klarade det på", försök, "försök!")
                        break

            elif game_choice == "2":
                print()
                print("===== SANT ELLER FALSKT =====")

                frågor = [
                    ["Sverige ligger i Europa.", "sant"],
                    ["Jorden är platt.", "falskt"],
                    ["Vatten fryser vid 0 grader Celsius.", "sant"],
                    ["Stockholm är Sveriges huvudstad.", "sant"],
                    ["Månen är större än jorden.", "falskt"],
                    ["En vecka har 7 dagar.", "sant"],
                    ["Solen är en planet.", "falskt"],
                    ["H2O är vatten.", "sant"],
                    ["En timme har 60 minuter.", "sant"],
                    ["Sverige ligger i Afrika.", "falskt"],
                    ["Är Pauli den bästa skolan?", "falskt"],
                    ["Skrattar David för mycket?", "sant"],
                    ["Överdriver Martin?", "sant"]
                ]

                poäng = 0

                for i in range(3):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Sant eller falskt? ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 3 rätt!")

            elif game_choice == "3":
                print()
                print("===== MATTE TÄVLING =====")

                poäng = 0

                for i in range(5):
                    number1 = random.randint(1, 20)
                    number2 = random.randint(1, 20)

                    räknesätt = random.choice(["+", "-", "*"])

                    print()
                    print("Fråga", i + 1)

                    if räknesätt == "+":
                        svar = float(input(str(number1) + " + " + str(number2) + " = "))
                        rätt_svar = number1 + number2

                    elif räknesätt == "-":
                        svar = float(input(str(number1) + " - " + str(number2) + " = "))
                        rätt_svar = number1 - number2

                    else:
                        svar = float(input(str(number1) + " * " + str(number2) + " = "))
                        rätt_svar = number1 * number2

                    if svar == rätt_svar:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", rätt_svar)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif game_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # HISTORIA ARCADE
    # =========================================================

    elif main_choice == "3":

        while True:
            print()
            print("===== HISTORIA ARCADE =====")
            print("1. Historiequiz")
            print("2. Vem är jag?")
            print("3. Gissa årtalet")
            print("4. Tillbaka till huvudmenyn")

            history_choice = input("Välj ett spel: ")

            if history_choice == "1":
                print()
                print("===== HISTORIEQUIZ =====")

                frågor = [
                    ["När började andra världskriget?", "1939"],
                    ["När slutade andra världskriget?", "1945"],
                    ["Vilket år började första världskriget?", "1914"],
                    ["Vilket år landade människan på månen?", "1969"],
                    ["Vilket år började Franska revolutionen?", "1789"],
                    ["Vem var Sveriges kung och grundade Vasaätten?", "Gustav Vasa"],
                    ["Vilket år föll Berlinmuren?", "1989"],
                    ["Vilket år blev Sverige medlem i EU?", "1995"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ")

                    if svar.lower() == fråga[1].lower():
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif history_choice == "2":
                print()
                print("===== VEM ÄR JAG? =====")

                personer = [
                    ["Jag var en svensk kung och grundade Vasaätten.", "Gustav Vasa"],
                    ["Jag var en svensk kung som dog i slaget vid Lützen.", "Gustav II Adolf"],
                    ["Jag var fransk kejsare och förlorade vid Waterloo.", "Napoleon"],
                    ["Jag var en egyptisk drottning som blev känd för sina relationer med romerska ledare.", "Kleopatra"]
                ]

                person = random.choice(personer)

                print(person[0])

                svar = input("Vem är jag? ")

                if svar.lower() == person[1].lower():
                    print("Rätt! 🎉")
                else:
                    print("Fel!")
                    print("Rätt svar var:", person[1])

            elif history_choice == "3":
                print()
                print("===== GISSA ÅRTALET =====")

                årtal = [
                    ["Andra världskriget börjar", 1939],
                    ["Första världskriget börjar", 1914],
                    ["Franska revolutionen börjar", 1789],
                    ["Människan landar på månen", 1969],
                    ["Berlinmuren faller", 1989],
                    ["Sverige blir medlem i EU", 1995]
                ]

                händelse = random.choice(årtal)

                print()
                print(händelse[0])

                svar = int(input("Vilket år hände detta? "))

                if svar == händelse[1]:
                    print("Rätt! 🎉")
                else:
                    print("Fel!")
                    print("Rätt år var:", händelse[1])

            elif history_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # ELTEKNIK
    # =========================================================

    elif main_choice == "4":

        while True:
            print()
            print("===== ELTEKNIK =====")
            print("1. Ohms lag")
            print("2. Elektrisk effekt")
            print("3. Elteknikquiz")
            print("4. Tillbaka till huvudmenyn")

            el_choice = input("Välj ett alternativ: ")

            if el_choice == "1":
                print()
                print("===== OHMS LAG =====")
                print("Formel: U = R × I")
                print("1. Räkna ut spänning")
                print("2. Räkna ut ström")
                print("3. Räkna ut resistans")

                val = input("Välj: ")

                if val == "1":
                    R = float(input("Resistans (Ω): "))
                    I = float(input("Ström (A): "))
                    print("Spänningen är:", R * I, "V")

                elif val == "2":
                    U = float(input("Spänning (V): "))
                    R = float(input("Resistans (Ω): "))

                    if R == 0:
                        print("Resistansen kan inte vara 0!")
                    else:
                        print("Strömmen är:", U / R, "A")

                elif val == "3":
                    U = float(input("Spänning (V): "))
                    I = float(input("Ström (A): "))

                    if I == 0:
                        print("Strömmen kan inte vara 0!")
                    else:
                        print("Resistansen är:", U / I, "Ω")

                else:
                    print("Det alternativet finns inte!")

            elif el_choice == "2":
                print()
                print("===== ELEKTRISK EFFEKT =====")
                print("Formel: P = U × I")

                U = float(input("Spänning (V): "))
                I = float(input("Ström (A): "))

                print("Effekten är:", U * I, "W")

            elif el_choice == "3":
                print()
                print("===== ELTEKNIKQUIZ =====")

                frågor = [
                    ["Vilken enhet mäts spänning i?", "volt"],
                    ["Vilken enhet mäts ström i?", "ampere"],
                    ["Vilken enhet mäts resistans i?", "ohm"],
                    ["Vilken enhet mäts effekt i?", "watt"],
                    ["Vad heter formeln U = R × I?", "ohms lag"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif el_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # DATOR OCH KOMMUNIKATIONSTEKNIK
    # =========================================================

    elif main_choice == "5":

        while True:
            print()
            print("===== DATOR OCH KOMMUNIKATIONSTEKNIK =====")
            print("1. Datorquiz")
            print("2. Nätverksquiz")
            print("3. Hårdvaruquiz")
            print("4. Tillbaka till huvudmenyn")

            computer_choice = input("Välj ett alternativ: ")

            if computer_choice == "1":
                print()
                print("===== DATORQUIZ =====")

                frågor = [
                    ["Vad står CPU för?", "central processing unit"],
                    ["Vad används RAM till?", "arbetsminne"],
                    ["Vad står SSD för?", "solid state drive"],
                    ["Vad används ett operativsystem till?", "styra datorn"],
                    ["Vad är GPU?", "grafikprocessor"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif computer_choice == "2":
                print()
                print("===== NÄTVERKSQUIZ =====")

                frågor = [
                    ["Vad står IP för?", "internet protocol"],
                    ["Vad används DNS till?", "översätta domännamn"],
                    ["Vad används en router till?", "skicka trafik mellan nätverk"],
                    ["Vad används Ethernet till?", "nätverksanslutning"],
                    ["Vad står LAN för?", "local area network"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif computer_choice == "3":
                print()
                print("===== HÅRDVARUQUIZ =====")

                frågor = [
                    ["Vilken komponent lagrar filer permanent?", "ssd"],
                    ["Vilken komponent utför beräkningar?", "cpu"],
                    ["Vilken komponent hanterar grafik?", "gpu"],
                    ["Vilken komponent används som arbetsminne?", "ram"],
                    ["Vad kopplar ihop komponenterna i datorn?", "moderkort"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif computer_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # PROGRAMMERING
    # =========================================================

    elif main_choice == "6":

        while True:
            print()
            print("===== PROGRAMMERING =====")
            print("1. Pythonquiz")
            print("2. Gissa output")
            print("3. Programmeringsbegrepp")
            print("4. Tillbaka till huvudmenyn")

            programming_choice = input("Välj ett alternativ: ")

            if programming_choice == "1":
                print()
                print("===== PYTHONQUIZ =====")

                frågor = [
                    ["Vilket kommando används för att skriva ut text?", "print"],
                    ["Vilket kommando används för att läsa input?", "input"],
                    ["Vilket kommando används för ett villkor?", "if"],
                    ["Vilken loop upprepas så länge ett villkor är sant?", "while"],
                    ["Vilket kommando används för att skapa en loop med ett bestämt antal gånger?", "for"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif programming_choice == "2":
                print()
                print("===== GISSA OUTPUT =====")

                frågor = [
                    ["x = 5\nprint(x + 3)", "8"],
                    ["x = 10\nprint(x * 2)", "20"],
                    ["x = 20\nprint(x - 5)", "15"],
                    ["x = 4\nprint(x * 3)", "12"]
                ]

                fråga = random.choice(frågor)

                print("Vad skriver programmet ut?")
                print()
                print(fråga[0])

                svar = input("Svar: ")

                if svar == fråga[1]:
                    print("Rätt! 🎉")
                else:
                    print("Fel!")
                    print("Rätt svar var:", fråga[1])

            elif programming_choice == "3":
                print()
                print("===== PROGRAMMERINGSBEGREPP =====")
                print("1. Variabel")
                print("2. Loop")
                print("3. If-sats")
                print("4. Lista")
                print("5. Tillbaka")

                val = input("Välj: ")

                if val == "1":
                    print("En variabel används för att lagra ett värde.")

                elif val == "2":
                    print("En loop används för att upprepa kod.")

                elif val == "3":
                    print("En if-sats används för att kontrollera ett villkor.")

                elif val == "4":
                    print("En lista kan innehålla flera värden.")

                elif val == "5":
                    break

                else:
                    print("Det alternativet finns inte!")

            elif programming_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # ENGELSKA
    # =========================================================

    elif main_choice == "7":

        while True:
            print()
            print("===== ENGELSKA =====")
            print("1. Glosor")
            print("2. Översättning")
            print("3. English quiz")
            print("4. Tillbaka till huvudmenyn")

            english_choice = input("Välj ett alternativ: ")

            if english_choice == "1":
                print()
                print("===== GLOSOR =====")

                ord = [
                    ["hund", "dog"],
                    ["katt", "cat"],
                    ["skola", "school"],
                    ["dator", "computer"],
                    ["nätverk", "network"],
                    ["bok", "book"],
                    ["fotboll", "football"],
                    ["lärare", "teacher"]
                ]

                poäng = 0

                for i in range(5):
                    ordet = random.choice(ord)

                    print()
                    print("Översätt:", ordet[0])

                    svar = input("Engelska: ").lower()

                    if svar == ordet[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", ordet[1])

                    ord.remove(ordet)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif english_choice == "2":
                print()
                print("===== ÖVERSÄTTNING =====")

                meningar = [
                    ["I have a computer.", "Jag har en dator."],
                    ["I play football.", "Jag spelar fotboll."],
                    ["The school is big.", "Skolan är stor."],
                    ["I like programming.", "Jag gillar programmering."],
                    ["The network is fast.", "Nätverket är snabbt."]
                ]

                mening = random.choice(meningar)

                print("Översätt till svenska:")
                print(mening[0])

                svar = input("Svar: ").lower()

                if svar == mening[1].lower():
                    print("Rätt! 🎉")
                else:
                    print("Fel!")
                    print("Rätt svar var:", mening[1])

            elif english_choice == "3":
                print()
                print("===== ENGLISH QUIZ =====")

                frågor = [
                    ["What is the opposite of 'big'?", "small"],
                    ["What is the English word for 'hund'?", "dog"],
                    ["What is the English word for 'skola'?", "school"],
                    ["What is the opposite of 'fast'?", "slow"],
                    ["What is the English word for 'fotboll'?", "football"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Question", i + 1)
                    print(fråga[0])

                    svar = input("Answer: ").lower()

                    if svar == fråga[1]:
                        print("Correct! 🎉")
                        poäng += 1
                    else:
                        print("Wrong!")
                        print("Correct answer was:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULT =====")
                print("You got", poäng, "out of 5 correct!")

            elif english_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # IDROTT
    # =========================================================

    elif main_choice == "8":

        while True:
            print()
            print("===== IDROTT =====")
            print("1. Idrottsquiz")
            print("2. Fotbollsquiz")
            print("3. Träningsquiz")
            print("4. Tillbaka till huvudmenyn")

            sport_choice = input("Välj ett alternativ: ")

            if sport_choice == "1":
                print()
                print("===== IDROTTSQUIZ =====")

                frågor = [
                    ["Hur många spelare har ett fotbollslag på planen?", "11"],
                    ["Hur många minuter är en vanlig fotbollsmatch?", "90"],
                    ["Hur många ringar finns på OS-symbolen?", "5"],
                    ["Vilken sport använder en basketboll?", "basket"],
                    ["Vilken sport använder en puck?", "ishockey"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif sport_choice == "2":
                print()
                print("===== FOTBOLLSQUIZ =====")

                frågor = [
                    ["Hur många spelare har ett lag på planen?", "11"],
                    ["Hur länge är en vanlig match?", "90 minuter"],
                    ["Vad kallas personen som dömer matchen?", "domare"],
                    ["Vad kallas det när en spelare gör tre mål?", "hattrick"],
                    ["Hur många halvlekar har en match?", "2"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif sport_choice == "3":
                print()
                print("===== TRÄNINGSQUIZ =====")

                frågor = [
                    ["Vad är viktigt att göra före hård träning?", "uppvärmning"],
                    ["Vad behöver kroppen för att kunna prestera?", "energi"],
                    ["Vad är viktigt efter träning?", "återhämtning"],
                    ["Vad transporterar syre i kroppen?", "blodet"],
                    ["Vilket organ pumpar runt blodet?", "hjärtat"]
                ]

                poäng = 0

                for i in range(5):
                    fråga = random.choice(frågor)

                    print()
                    print("Fråga", i + 1)
                    print(fråga[0])

                    svar = input("Ditt svar: ").lower()

                    if svar == fråga[1]:
                        print("Rätt! 🎉")
                        poäng += 1
                    else:
                        print("Fel!")
                        print("Rätt svar var:", fråga[1])

                    frågor.remove(fråga)

                print()
                print("===== RESULTAT =====")
                print("Du fick", poäng, "av 5 rätt!")

            elif sport_choice == "4":
                break

            else:
                print("Det alternativet finns inte!")

    # =========================================================
    # AVSLUTA
    # =========================================================

    elif main_choice == "9":
        print("Hejdå! 👋")
        break

    else:
        print("Det alternativet finns inte!")

