principal = 0
time = 0
rate_of_interest = 0
final_amount = 0

while(principal <= 0):
    principal = float(input("Enter the principal: "))

    if principal <= 0:
        print("Principal can't not be zero or less than zero")

while(rate_of_interest <= 0):
    rate_of_interest = float(input("Enter the rate of interest: "))

    if rate_of_interest <= 0:
        print("Rate of interest can't not be zero or less than zero")

while(time <= 0):
    time = float(input("Enter the time(in year): "))

    if time <= 0:
        print("Time can't not be zero or less than zero")



final_amount = principal*((1+ rate_of_interest/100)**time)
print(f"You owe ${final_amount}")