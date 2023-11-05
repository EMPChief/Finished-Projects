# The code is importing the `time` module and then running a nested loop.
import time
for a in range(3):
    for b in range(1, 101):
        print(b, end=", ")
    time.sleep(10)
    print("\n")