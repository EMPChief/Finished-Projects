# The code is using a while loop to decrement the value of the variable `hamster` by 1 each time
# through the loop. It will continue looping as long as `hamster` is greater than 0. Inside the loop,
# it will print the current value of `hamster` using an f-string. Once `hamster` reaches 0, the loop
# will exit and it will print "You left the loop".

hamster = 10

while hamster > 0:
    hamster -= 1
    print(f"One number gone {hamster}")
print("You left the loop")
