# This code is creating an empty list called `foods`. It then enters a while loop that continues until
# the user enters "quit" (case-insensitive). Inside the loop, it prompts the user to enter a food they
# like and assigns it to the variable `food` using the walrus operator `:=`. It then appends the
# entered food to the `foods` list. Once the user enters "quit", the loop exits and the code prints
# the contents of the `foods` list.
foods = []

while (food := input("What food do you like? (quit to stop program) ")).lower() != "quit":
    foods.append(food)

print(foods)