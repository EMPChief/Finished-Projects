
double = lambda x: x * 2
print(double(5))


multiply_babes = lambda a, b: a * b
multiply_fun = lambda a, b, c: a * b * c
print(f"Your going to have so much fun: {multiply_fun(2, 3, 4)} times")
print(f"Your getting {multiply_babes(2, 3)} babes")

age_check = lambda age: age >= 18

print(f"Your age is not over 18: {not age_check(18)}")

