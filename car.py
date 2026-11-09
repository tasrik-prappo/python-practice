class Car:
    def __init__(self,model: str, year: int, color: str, for_sale: bool):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def start(self):
        print("Car is starting....")

    def stop(self):
        print("Car is stopping....")

    def show_info(self):
        print(f"Car model: {self.model}\nYear of buying: {self.year}\nCar Color: {self.color}\n {"Car is for sale" if self.for_sale else "Car is not for sale"}")

