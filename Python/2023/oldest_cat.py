class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age} year old animal."

    def __call__(self, name, age):
        return Animal(name, age)

    def make_noise(self):
        return "Animal makes a noise."

    def eat(self, food):
        return f"{self.name} eats {food}."

    def sleep(self):
        return f"{self.name} is sleeping."

    def play(self):
        return f"{self.name} is playing."

    def go_to_the_bathroom(self):
        return f"{self.name} is going to the bathroom."

    def get_medical_attention(self):
        return f"{self.name} is getting medical attention."

    def die(self):
        return f"{self.name} has died."


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed} cat."

    def make_noise(self):
        return "Meow!"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed} dog."

    def make_noise(self):
        return "Woof!"


class Fish(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species} fish."

    def make_noise(self):
        return "Fish makes a noise."


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species} bird."

    def make_noise(self):
        return "Bird makes a noise."


class Reptile(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species} reptile."

    def make_noise(self):
        return "Reptile makes a noise."


cat = Cat("Mittens", 2, "Persian")
dog = Dog("Buddy", 3, "Golden Retriever")
fish = Fish("Bubbles", 1, "Goldfish")
bird = Bird("Polly", 5, "Parrot")
reptile = Reptile("Snappy", 10, "Snake")

print(cat)
print(dog)
print(fish)
print(bird)
print(reptile)

# Create 20 different instances with different animals, names, and ages

animals = [cat, dog, fish, bird, reptile]
names = ["Mittens", "Buddy", "Bubbles", "Polly", "Snappy"]
ages = [2, 3, 1, 5, 10]

for i in range(20):
    animal = animals[i % 5]
    name = names[i % 5]
    age = ages[i % 5]
    print(animal(name, age))
