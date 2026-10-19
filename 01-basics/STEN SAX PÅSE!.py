import random

# Statistics
wins = 0
losses = 0
draws = 0
winstreak = 0
best_winstreak = 0

# Menu
print("ROCK PAPER SCISSORS")
print("1. Infinite rounds")
print("2. 3 rounds")
print("3. 10 rounds")

# Ask the player how many rounds they want to play
choice = input("Choose the number of rounds: ")

# Choose the number of rounds
if choice == "1":
    rounds = 0 
elif choice == "2":
    rounds = 3
elif choice == "3":
    rounds = 10
else:
     # Stops the game if a invalid choice has happend.
    rounds = -1
    print("Invalid choice!")
  

# Counts how many rounds have been played
round_number = 0

# Game loop
# Continue while the game has rounds left to play 
while rounds == 0 or round_number < rounds:

    # Stop the game if the player chose an invalid option
    if rounds == -1:
        break

    # Show the current round and winning streak
    print("\nRound", round_number + 1)
    print("Winning streak:", winstreak)

    # Ask the player to choose rock, paper, scissors or quit
    hand = input("Rock, paper, scissors or quit? ").capitalize()

    # Stops the game if the player wants to quit
    if hand == "Quit":
        break

    # Check if players choice is valid
    if hand == "Rock" or hand == "Paper" or hand == "Scissors":

        # The computer randomly chooses a number from 1 to 3
        computer = random.randint(1, 3)

        # Convert the random number into a hand
        if computer == 1:
            computer_hand = "Rock"
        elif computer == 2:
            computer_hand = "Paper"
        else:
            computer_hand = "Scissors"

        # Shows choices
        print("You chose:", hand)
        print("The computer chose:", computer_hand)

        # Add one to the number of played rounds
        round_number += 1

        # Check if the round is a draw
        if hand == computer_hand:
            print("It's a draw!")
            draws += 1

        # Check if the player wins with rock
        elif hand == "Rock" and computer_hand == "Scissors":
            print("You won!")
            wins += 1
            winstreak += 1

        # Check if the player wins with paper
        elif hand == "Paper" and computer_hand == "Rock":
            print("You won!")
            wins += 1
            winstreak += 1

        # Check if the player wins with scissors
        elif hand == "Scissors" and computer_hand == "Paper":
            print("You won!")
            wins += 1
            winstreak += 1

        # If none of the above conditions are true, the player loses
        else:
            print("You lost!")
            losses += 1

            # Reset the winning streak after a loss
            winstreak = 0

        # Save the best winning streak if the current one is higher
        if winstreak > best_winstreak:
            best_winstreak = winstreak

    else:
        # Tell the player if they entered an invalid choice
        print("Invalid choice! Try again.")

# Shows the statistics when the game ends
print("GAME OVER")
print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)
print("Current winning streak:", winstreak)
print("Best winning streak:", best_winstreak)
