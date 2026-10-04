class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Predator(Animal):

    def hunt(self):
        print(f"{self.name} is hunting")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is running away")

class Lion(Predator):
    pass

class Deer(Prey):
    pass

class Fish(Predator,Prey):
    pass

lion = Lion("Simba")
deer = Deer("Roach")
fish = Fish("Neo")

lion.eat()
deer.flee()
fish.hunt()
fish.flee()
lion.hunt()
deer.sleep()