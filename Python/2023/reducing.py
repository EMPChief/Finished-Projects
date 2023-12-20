import functools
list = ['H', 'E', 'L', 'L', 'O', ' ', 'S', 'T', 'E', 'V', 'E', 'N']


word = functools.reduce(lambda x, y: x + y, list)

print(word)

factorial = [8, 7, 6, 5, 4, 3, 2, 1, 10, 12, 14]

result = functools.reduce(lambda x, y: x * y, factorial)
print(result)


squares = [a * a for a in range(1, 20)]
print(squares)
students = [90, 53, 79, 21, 23, 56, 79]

passed_students = [b if b >= 45 else "Failed" for b in students]
print(f"Checking if failed or passed: {passed_students}")

friendrly = ['Frida', 'Frida', 'Mathilda', 'Robin', 'Robin', 'Clara', 'Clara']
checkfriendly = [c for c in friendrly if friendrly.count(c) >= 2]
print(
    f"Checking how many time friend is mentioned, if more then 2 print: {checkfriendly}")
