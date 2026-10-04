<<<<<<< HEAD
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


    
=======
<<<<<<< HEAD
Week = 3500
CoffeeBikeFood = 1500
ShirtPerfumeShampooSoapPantETCS = 2000
Bus = 3000
print(Week+CoffeeBikeFood+ShirtPerfumeShampooSoapPantETCS+Bus)


=======
n = 5
if n%2 != 0:
    print("Weird")
elif n%2 == 0 & n >= 2 & n <=5:
    print("Not Weird")
elif n%2 == 0 & n >=6 & n <= 20:
    print("Weird")
elif n%2 == 0 & n > 20:
    print("Not Weird")
>>>>>>> 0fc01dafe1e1cace50bc3e3cfef126c268af6db5
>>>>>>> a8831a6c37af81df23f05c3bef629f04d48a02a3
