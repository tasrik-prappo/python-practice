def receipt_generator(*prices: float, **details: str) -> str:
    total: float = 0.0
    information: str = ""

    for price in prices:
        total += price

    for key, value in details.items():
        information += f"{key.replace('_', ' ').capitalize()}: {value}\n"

    return f"Total bill: ${total}\nCustomer information:\n{information.strip()}"


print(receipt_generator(100, 600, 80, 4000, name="Prappo", city="Dhaka", payment_method="Cash"))