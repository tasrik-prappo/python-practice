import random

high: int = 10
low: int = 1
guess_count: int = 0

answer: int = random.randint(low,high)

while True:

    guess: str = input("Enter your guess: ")

    if guess.isdigit():
        guess: int = int(guess)
        guess_count += 1
        if guess == answer:
            print(f"You GUESSED CORRECTLY!!! The number was {answer}. You took {guess_count} guesses")
            break
        elif guess < low or guess > high:
            print(f"Warning!! Please guess the number between {low} and {high}")
        elif guess < answer:
            print("Too low. Try again")
        elif guess > answer:
            print("Too high. Try again")
    else:
        print("Enter an integer. Try again")
        