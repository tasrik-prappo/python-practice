class Animal:

    def __init__(self,name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")

    def isAlive(self):
        print(f"{self.name} is alive")

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("Bob")
cat = Cat("Tom")
mouse = Mouse("Jerry")

dog.eat()
cat.sleep()
mouse.isAlive()
