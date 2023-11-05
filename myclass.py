# The above class defines a car object with attributes such as make, model, year, color, and speed,
# and methods to drive and stop the car.



class car:
    def __init__(self, make, model, Year, color, speed):
        self.make = make
        self.model = model
        self.Year = Year
        self.color = color
        self.speed = speed
    def drive(self):
        print(f"This {self.model} is driving")
    def stop(self):
        print(f"This {self.model} is stopped")