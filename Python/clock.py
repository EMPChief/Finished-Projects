# This code is a Python program that takes an input from the user for a time in seconds. It then
# counts down from that time, printing the remaining time in the format "HH:MM:SS" (hours, minutes,
# seconds) with leading zeros. The program uses the `time` module to pause the execution for 1 second
# between each countdown. Once the countdown is complete, it prints the message "Hard time is over,
# time to relax a little bit".
import time

time_input = int(input("Input a time in seconds:"))

for  a in range(time_input, 0, -1):
    seconds = a % 60
    minutes = (a // 60) % 60
    hours = (a // 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Hard time is over, time to relax a little bit")