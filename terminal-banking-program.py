def show_balance(balance: float) -> None:
    print(f"Your current balance is ${balance:.2f}")

def deposit() -> float:
    add_balance: str = input("Enter the ammount: ")
    add_balance: float = float(add_balance)

    if add_balance < 0:
        print("Not a valid number")
        return 0
    else:
        return add_balance

def withdraw(current_balance: float) -> float:
    amount: float = float(input("How much do you want to withdraw: "))
    
    if current_balance < amount:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance: float = 0.0
 

    while True:
        print("---------------------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("---------------------")
        print()
        choice: str = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        
        elif choice == "2":
            balance += deposit()
        
        elif choice == "3":
            balance -= withdraw(balance)
        
        elif choice == "4":
            break

        else:
            print("Invalid choice")

    print("Thank you. Have a nice day")




if __name__ == "__main__":
    main()


