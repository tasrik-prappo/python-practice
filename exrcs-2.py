price_1 = float(input("Enter price of product 1: "))
price_2 = float(input("Enter price of product 2: "))
price_3 = float(input("Enter price of product 3: "))

total_bill = price_1 + price_2 + price_3
average = total_bill / 3

print(f"Total bill: {total_bill}")
print(f"Average price: {average}")

superhero_name = input("Enter a super hero name: ")

if superhero_name.lower().startswith('s'):
    print("Superhero name starts with S")
else:
    print("Superhero name doesn't start with S")