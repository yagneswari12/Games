print("Welcome to my computer quiz game!")
playing = input("Do you want to play : ").lower()

score = 0

if playing != "yes":
   quit()

print("Okay Let's play the game :) ")

answer = input("Who is the father of computer? ").lower()
if answer == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does WPN stands for? ").lower()
if answer == "wide area network":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got "+str(score)+" questions correct! ")
if score == 5:
    print("Excellent!")
else:
    print("Better luck next time!")



