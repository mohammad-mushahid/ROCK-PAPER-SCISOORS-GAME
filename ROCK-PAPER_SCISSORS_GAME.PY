import random
choices = ["rock", "paper", "scissors"]
user = input("Enter rock, paper, scisoors: ")
computer = random.choice(choices)
print("Computer choose:", computer)
if user == computer:
    print("Draw")

elif user == "rock" and computer == "scisoors":
    print("You win")

elif user == "paper" and computer == "rock":
    print("You win")

elif user == "scisoors" and computer == "paper":
    print("You win")

else:
 print("You lose")
