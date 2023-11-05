# The code defines a class hierarchy for different types of animals, with specific behaviors for each
# type.
class Animal:
    alive = True
    def __init__(self, name=None, age=None, weight=None, legs=None, type=None, color=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.legs = legs
        self.type = type
        self.color = color
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def breathe(self):
        print(f"{self.name} is breathing")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking alot")

class Cat(Animal):
    def hunt(self):
        print(f"{self.name} can hunt very good")

class Rabbit(Animal):
    def run(self):
        print(f"{self.name} can run very fast")

class Horse(Animal): 
    def jump(self):
        print(f"{self.name} can juump very high")

class Hawk(Animal):
    def fly(self):
        print(f"{self.name} can fly very fast")