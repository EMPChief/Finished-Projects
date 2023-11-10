import time

print(time.ctime(0))
time_object = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", time_object))
print(time_object)

time_tuple = (2019, 10, 20, 10, 15, 10, 15, 15, -1)
time_string = time.asctime(time_tuple)
time_fun = time.mktime(time_tuple)
print(time_fun)
print(time_string)