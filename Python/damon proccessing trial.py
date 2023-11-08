import time
import threading
import datetime
#
#def time_logged_in():
#    print()
#    count = 0
#    while True:
#        time.sleep(1)
#        count += 1
#        print(f"Logged in {count} seconds")
#        
#x = threading.Thread(target=time_logged_in, daemon=True)
#x.start()
#exit = input("Do you want to exit? (y/n): ")

def time_logged_in():
    count = 0
    time.sleep(1)
    while True:
        count += 1
        with open("time.txt", "a") as f:
            f.write(f"Logged in {count:.2f} seconds\n")
        time.sleep(1)
x = threading.Thread(target=time_logged_in, daemon=True)
x.start()

exit = input("Do you want to exit? (y/n): ")