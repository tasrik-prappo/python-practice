class Car:

    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def start(self):
        print(f"{self.model} is starting")

    def stop(self):
        print(f"{self.model} is stopping")

    def show_info(self):
        print(f"Car name: {self.model}\nBuying year: {self.year}\nCar color: {self.color}\n")
        if(self.for_sale):
            print("Car is for sale")
        else:
            print("Car is not for sale")

car1 = Car("BMW", 2028, "red", False)
print(car1.model)
car1.start()
car1.show_info()


    