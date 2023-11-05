# The code is importing the `car` class from the `myclass` module. It then creates four instances of
# the `car` class (`car_1`, `car_2`, `car_3`, `car_4`) with different attributes such as make, model,
# year, color, and speed.
from myclass import car



car_1 = car("Ford", "Mustang", 2020, "purple", 100)
car_2 = car("Toyota", "Land Cruiser", 1999, "blue", 0)
car_3 = car("Volkswagen", "Volkswagen Golf GTi", 2021, "red", 120)
car_4 = car("BMW", "X500", 2019, "green", 0)

print(f"Maker: {car_1.make}, Model: {car_1.model}, Year: {car_1.Year}, Color: {car_1.color}, Speed: {car_1.speed}")
car_1.drive()
print(f"Maker: {car_2.make}, Model: {car_2.model}, Year: {car_2.Year}, Color: {car_2.color}, Speed: {car_2.speed}")
car_2.stop()
print(f"Maker: {car_3.make}, Model: {car_3.model}, Year: {car_3.Year}, Color: {car_3.color}, Speed: {car_3.speed}")
car_3.drive()
print(f"Maker: {car_4.make}, Model: {car_4.model}, Year: {car_4.Year}, Color: {car_4.color}, Speed: {car_4.speed}")
car_4.stop()