
def double(x): return x * 2


print(double(5))


def multiply_babes(a, b): return a * b
def multiply_fun(a, b, c): return a * b * c


print(f"Your going to have so much fun: {multiply_fun(2, 3, 4)} times")
print(f"Your getting {multiply_babes(2, 3)} babes")


def age_check(age): return age >= 18


print(f"Your age is not over 18: {not age_check(18)}")
