# The code `from animal_class import *` is importing all the classes and functions defined in the
# `animal_class` module. This allows us to use the classes `Rabbit`, `Dog`, `Cat`, `Horse`, and `Hawk`
# in our code.
from animal_class import *
# The code is creating instances of different animal classes (`Rabbit`, `Dog`, `Cat`, `Horse`, and
# `Hawk`) and initializing them with specific attributes. Each animal instance is then printed with
# its name, alive status, age, weight, number of legs, color, type, and speciality.

rabbit = Rabbit("James The Rabbit", 1, 3, 4, "Alaskan", "White")
dog = Dog("Adam", 4, 5, 4, "White Shepherd")
cat = Cat("Mia", 10, 3, 4, "Birman", "Yellow White")
horse = Horse("Blazer", 15, 500, 4, "Akhal-Teke", "Brown")
hawk = Hawk("Bird of Prey", 5, 1.6, 2, "Red Tailed Hawk", "Red")

print(f"Rabbit: {rabbit.name}, Alive: {rabbit.alive}, Age: {rabbit.age}, Weight: {rabbit.weight}, Legs: {rabbit.legs}, Color: {rabbit.color}, Type:{rabbit.type}, Speciality: {rabbit.run}")
print(f"Dog: {dog.name}, Alive: {dog.alive}, Age: {dog.age}, Weight: {dog.weight}, Legs: {dog.legs}, Color: {dog.color}, Type:{dog.type}, Speciality: {dog.bark}")
print(f"Horse: {horse.name}, Alive: {horse.alive}, Age: {horse.age}, Weight: {horse.weight}, Legs: {horse.legs}, Color: {horse.color}, Type:{horse.type}, Speciality: {horse.jump}")
print(f"Cat: {cat.name}, Alive: {cat.alive}, Age: {cat.age}, Weight: {cat.weight}, Legs: {cat.legs}, Color: {cat.color}, Type:{cat.type}, Speciality: {cat.hunt}")
print(f"Hawk: {hawk.name}, Alive: {hawk.alive}, Age: {hawk.age}, Weight: {hawk.weight}, Legs: {hawk.legs}, Color: {hawk.color}, Type:{hawk.type}, Speciality: {hawk.fly}")
