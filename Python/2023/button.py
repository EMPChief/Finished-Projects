from tkinter import *


count = 0


def clicked_shit():
    global count
    count += 1
    print(f"You really clicked it :O\nYou clicked it {count} times")


empbutton = Tk()
image = PhotoImage(file="logo.png")
empbutton = Button(empbutton,
                   text="I know you really want to click the shit out off this button!",
                   command=clicked_shit,
                   font=("Arial", 20, "bold"),
                   fg="blue",
                   bg="black",
                   activebackground="green",
                   activeforeground="black",
                   image=image,
                   compound='bottom'
                   )

empbutton.pack()

empbutton.mainloop()
