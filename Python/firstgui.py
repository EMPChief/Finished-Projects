from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Hello World")
window.configure(background="Red")
window.resizable(True, True)
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.mainloop()
