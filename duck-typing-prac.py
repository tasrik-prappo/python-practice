class Animal:

    isAlive = True

class Dog(Animal):

    def speak(self):
        print("WOOF!")

class Cat(Animal):

    def speak(self):
        print("MEOW!")

class Car:

    isAlive = False

    def speak(self):
        print("HONK!")

animals = []