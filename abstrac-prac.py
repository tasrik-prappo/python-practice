from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print(f"{self.name} is starting")

    def stop(self):
        print(f"{self.name} is stopping")

class Bike(Vehicle):

    def start(self):
        print(f"{self.name} is starting")

    def stop(self):
        print(f"{self.name} is stopping")

car = Car("BMW")
bike = Bike("R15")

car.start()
bike.stop()