import random
from words import HANGMAN_ART, WORDS

def display_hint(hint: list[str]) -> None:
    print(" ".join(hint))

def display_hangman_art(wrong_guesses: int) -> None:
    print("---------------------------------")
    for line in HANGMAN_ART[wrong_guesses]:
        print(line)
    print("---------------------------------")


def main() -> None:
    answer: str = random.choice(WORDS).lower()
    hint: list[str] = ["_"] * len(answer)
    guessed_letters: set[str] = set()
    wrong_guesses: int = 0
    life: int = 6


    while True:
        display_hangman_art(wrong_guesses)
        display_hint(hint)

        print("Guess the word")
        guess: str = input("Enter your guess: ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} already been guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if guess == answer[index]:
                    hint[index] = guess
        else:
            print("Wrong GUESS!")
            print(f"Lives remaining: {life - wrong_guesses -1}")
            wrong_guesses += 1

        if wrong_guesses == life:
            display_hangman_art(wrong_guesses)
            print(f"The word was {answer}")
            print("You LOSE!")
            print("Thank you for playing")
            break


        if '_' not in hint:
            print(f"The word was {answer}")
            print("You WIN!")
            print("Thank you for playing")
            break


if __name__ == '__main__':
    main()