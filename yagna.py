import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print("Welcome to the game!")
user_name = input("Your name: ")

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked:",computer_pick + ".")

    if user_input == computer_pick:
        print("the game is a tie")

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print(user_name,"!You won",user_wins,"times.")
print("computer won",computer_wins,"times.")

if user_wins > computer_wins:
    print("The final winner is",user_name)
elif user_wins < computer_wins:
    print("Sorry! you lost")
    print("Better luck next time!")
else:
    print("No one is winner,The game is tie")