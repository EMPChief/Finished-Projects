do_you_have_fun = str(input("Do you have fun? (y/n): ")).lower()

if do_you_have_fun == "y" or do_you_have_fun == "yes":
    print("You must be having a blast!")
elif do_you_have_fun == "n" or do_you_have_fun == "no":
    print("You must not be having a blast!")
else:
    print("Shithead you can only type yes or no, y/n")