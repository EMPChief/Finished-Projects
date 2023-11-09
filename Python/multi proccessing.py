from multiprocessing import Process
import time

def counting_chicken(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counting_chicken, args=(500000000,))
    a.start()
    
    b = Process(target=counting_chicken, args=(500000000,))
    b.start()
    c = Process(target=counting_chicken, args=(500000000,))
    c.start()
    
    d = Process(target=counting_chicken, args=(500000000,))
    d.start()
    a.join()
    b.join()
    c.join()
    d.join()
    print(f"How many chickens counted every seconds: {time.perf_counter()}")

if __name__ == '__main__':
    main()