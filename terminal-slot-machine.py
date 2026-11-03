import random

def get_payout(sequence: list[str], bet: float) -> float:
    if sequence == ["🍒", "🍒", "🍒"]:
        return bet * 3
    elif sequence == ["🍉", "🍉", "🍉"]:
        return bet * 4
    elif sequence == ["🍋", "🍋", "🍋"]:
        return bet * 5
    elif sequence == ["🔔", "🔔", "🔔"]:
        return bet * 10
    elif sequence == ["⭐", "⭐", "⭐"]:
        return bet * 20
    else:
        return 0.0

def place_bet(balance: float) -> float:
    while True:
        try:
            bet: float = float(input("Enter the amount of bet you want to place: "))
            if bet <= 0:
                print("Bet has to be more than 0")
            elif bet > balance:
                print("Insufficient balance. Try again")
            else:
                return bet
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def show_balance(balance: float) -> None:
    print(f"Your current balance is ${balance:.2f}")

def main() -> None:
    balance: float = 100.0
    symbols: list[str] = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    while True:
        show_balance(balance)
        bet: float = place_bet(balance)

        balance -= bet
        sequence: list[str] = random.choices(symbols, k=3)
        print(f"The result is {' | '.join(sequence)}")

        payout: float = get_payout(sequence, bet)

        if payout > 0:
            print(f"You won ${payout:.2f}")
            balance += payout
        else:
            print(f"You lost ${bet:.2f}")

        if balance <= 0.0:
            print("Your balance is empty. You can not play")
            break

        choice: str = input("Do you want to continue playing(Y/N): ")
        if choice.lower() == 'n':
            break
        elif choice.lower() != 'y':
            print("Invalid input. Starting the game again")

    print(f"Thank you! You can check out ${balance:.2f}.")

if __name__ == '__main__':
    main()