import random

if __name__ == "__main__":

    computer = random.choice(["rock", "scissors", "paper"])

    user = input("your choice? ")

    print(computer)

    result = "tied"

    if user == "rock" and computer == "scissors":
        result = "win"
    elif user == "scissors" and computer == "paper":
        result = "win"
    elif user == "paper" and computer == "rock":
        result = "win"
    elif computer == "rock" and user == "scissors":
        result = "lose"
    elif computer == "scissors" and user == "paper":
        result = "lose"
    elif computer == "paper" and user == "rock":
        result = "lose"

    print("You", result)
