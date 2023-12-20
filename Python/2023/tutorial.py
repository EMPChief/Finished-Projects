# # #Lambda squaring
# # my_list = [4, 8, 12, 16, 20, 24]
# # print(list(map(lambda item: item ** 2, my_list)))

# # #lambda sorting
# # a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# # print(list(sorted(a, key=lambda x: x[1])))




# # #List comphernsion print duplicates
# # a_list = ['a', 'a', 'b', 'b', 'c', 'd', 'e', 'g', 'e', 'a', 'b', 'c', 'd', 'e',]
# # duplications = [item for item in set(a_list) if a_list.count(item) > 1]
# # print(duplications)


# # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#     def check_valid(*args, **kwargs):
#         if args[0]["valid"] == True:
#             return fn(*args, **kwargs)
#         else:
#             print("You are not logged in")
#     return check_valid

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)

# My range
# class MyRange():
#     current = 0
    
#     def __init__(self, first=None, last=None):
#         self.first = first
#         self.last = last
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyRange.current < self.last:
#             number = MyRange.current
#             MyRange.current += 1
#             return number
#         raise StopIteration

# for number in MyRange(0, 100000):
#     print(number)

# Calculate the fibonacci numbers and return them a list
# def fibonacci_list(n = 0):
#     fib_numbers = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_numbers.append(a)
#         a, b = b, a + b
#     return fib_numbers

# fib = fibonacci_list(2100)
# print(fib)
# Calculate the fibonacci numbers and return them as a string
# def fibonacci(n = 0):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b
#     return "Fibonacci numbers are finished counting"

# fib2 = fibonacci(210)
# print(fib2)

