def multipayer(a):
    def multi(b):
        return a * b
    return multi


multi = multipayer(2)
print(multi(3))
