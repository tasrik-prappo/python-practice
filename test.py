def place_bet(balance: float) -> float:
    while True:
        try:
            bet: float = float(input("Enter the amount of bet you want to place: "))
            break  
        except ValueError:
            print("Invalid input! Please enter a whole number.")

place_bet(1000)