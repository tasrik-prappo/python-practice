user_balance = 5.00
request_cost = 1.25

if request_cost > user_balance:
    print(f"Insufficient balance! Request costs ${request_cost}, but you only have {user_balance}")

elif user_balance == 0:
    print("Account empty. Please add funds")

else:
    user_balance -= request_cost
    print(f"Request approved! Remaining Balance: ${user_balance}")