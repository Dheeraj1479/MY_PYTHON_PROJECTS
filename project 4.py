import random
computer = ["Rock", "Paper", "Scissor"]
print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor")
choice = int(input())
computer = random.choice(computer)
if choice == 0 and computer == "Rock":
    print("Its a draw!")
elif choice == 0 and computer == "Paper":
    print("You lose!")
elif choice == 0 and computer == "Scissor":
    print("You win!")
elif choice == 1 and computer == "Rock":
    print("You win!")
elif choice == 1 and computer == "Paper":
    print("Its a draw!")
elif choice == 1 and computer == "Scissor":
    print("You lose!")
elif choice == 2 and computer == "Rock":
    print("You lose!")
elif choice == 2 and computer == "Paper":
    print("You win!")
elif choice == 2 and computer == "Scissor":
    print("Its a draw!")
else:
    print("You entered an invalid number! You lose!")


