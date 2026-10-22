menu: dict = {
    "Pizza"       :10,
    "Burger"      :6.75,
    "Nachos"      : 3,
    "Coke"        : 0.20,
    "Fried Rice"  : 2.50,
    "Vegetable" : 1.75,
    "Soup"        : 4.75,
    "Popcorn"    : 1.30
}

total_bill: float = 0
total_order: list = []

print("----------------MENU----------------")
for item in menu:

    print(f" {item} : ${menu[item]}")
    

print("--------------------------------")
while True:

    order: str = input("Select an item (q to quit): ")

    if order.lower() == 'q':
        print("-------------Your order-----------")
        print(", ".join(total_order))

        print()    
        print(f"Your total bill is ${total_bill}")
        break

    order = order.title()
    if order in menu:
        total_order.append(order)
        total_bill += menu[order] 
            