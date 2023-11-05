# The code is creating a list called `my_fruit_list` which contains various fruit names. It then
# performs several operations on the list, such as appending a new fruit, sorting the list, checking
# if a specific fruit is in the list, and getting the length of the list.
my_fruit_list = ["Banana", "Orange", "Apple", "Mango", "Pineapple", "Grape", "Strawberry", "Kiwi", "Mango", "Pineapple", "Grape",  "Strawberry", "apple"]


#my_fruit_list.append("Pineapple")
#print(my_fruit_list)
#my_fruit_list.sort()
#print(my_fruit_list)
#print("apple" in my_fruit_list)
#print(len(my_fruit_list))
#print(help(my_fruit_list))
#print(dir(my_fruit_list))
"""
for a in range(3):
    for list in my_fruit_list:
        print(list, end = " ")
    print()
"""

menu = {"cake": 99.50,
        "pizza": 22.20,
        "hotdog": 18.10,
        "burger": 15.80,
        "fries": 12.20,
        "pasta": 4.10,
        "chicken": 17.60,
        "fried rice": 19.20,
        "fried chicken": 3.10,
        "soda": 2.10,
        "fried pizza": 5.70}

cart =  []
total = 0
print("---------menu----------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("-----------------------")

while True:
    food = input("Enter the name of the food you want to order: (q to quit) ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)
print("-------your order-------")
for food in cart:
    total += menu.get(food)
    print(f"{food:15}: ${menu.get(food):.2f}")
    print(f"Total: ${total:.2f}")
print("-----------------------")