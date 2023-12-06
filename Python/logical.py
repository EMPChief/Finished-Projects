is_magican = True
is_expert = False

if is_magican and is_expert:
    print("You are a expert magican!")

elif is_magican and not is_expert:
    print("Your a magican, but you need experience!")

elif not is_magican:
    print("You are not an magican!")

else:
    print("Your nothing!")


my_list = [1, 2, 3, 4, 5, 6]
total_sum = 0
for item in my_list:
    total_sum += item
print(f"Total sum from my_list is: {total_sum}")

for i, char in enumerate(my_list):
    print(f"{i}: {char}")
