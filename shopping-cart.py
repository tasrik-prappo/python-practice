foods: list = []
prices: list = []


while True:

    food: str = input("Enter food name(enter q to exit): ")
    if food == 'q' or food == 'Q':
        break
    foods.append(food)
    price: str = float(input("Enter the price of the food: "))
    prices.append(price)

print(f"Items: {' ,'.join(foods)}")

index: int = prices.index(max(prices))
print(f"Most expensive: {foods[index]} ({prices[index]:.2f})")

print(f"Total: {sum(prices)}")
