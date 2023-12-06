from tkinter import *

give_me_your_name = input("I demand your name: ")
emp_labeling = Tk()
photo = PhotoImage(file='logo.png')
label = Label(emp_labeling,
              text=f"Hello There {give_me_your_name}\nDo you even lift?",
              font=('helvetica', 50, 'bold'),
              bg='red',
              fg='black',
              bd=20,
              relief=RAISED,
              padx=10,
              pady=10,
              image=photo,
              compound='right')
label.pack()
# label.place(x = 50, y = 100)

emp_labeling.mainloop()
