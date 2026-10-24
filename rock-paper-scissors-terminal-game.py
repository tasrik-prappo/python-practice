import random

options: tuple = ("rock","paper","scissors")


while True:

    computer_move: str = random.choice(options)
    user_move: str = input("Enter rock or paper or scissors: ")

    if user_move.lower() == computer_move:
        print(f"Your move {user_move}\nComputer's move {computer_move}\nIt is a TIE!")
    elif user_move.lower() == "rock" and computer_move == "scissors":
        print(f"Your move {user_move}\nComputer's move {computer_move}\nYou WIN!")
    elif user_move.lower() == "rock" and computer_move == "paper":
        print(f"Your move {user_move}\nComputer's move {computer_move}\nYou LOSE!")
    elif user_move.lower() == "paper" and computer_move == "rock":
        print(f"Your move {user_move}\nComputer's move {computer_move}\nYou WIN!")
    elif user_move.lower() == "paper" and computer_move == "scissors":
        print(f"Your move {user_move}\nComputer's move {computer_move}\nYou LOSE!")
    elif user_move.lower() == "scissors" and computer_move == "paper":
        print(f"Your move {user_move}\nComputer's move {computer_move}\nYou WIN!")
    elif user_move.lower() == "scissors" and computer_move == "rock":
        print(f"Your move {user_move}\nComputer's move {computer_move}\nYou LOSE!")
    else:
        print("Invalid input")
        continue

    wish: str = input("Do you want to continue playing(y/n): ")
    if wish.lower() == "y":
        pass
    elif wish.lower() == "n":
        break
    else:
        print("Invalid input. Game starting again....")
        continue



