import tkinter
from tkinter import *


def teste():
    print("Teste")


root = Tk()
root.title("Color Changer")

button = tkinter.Button(root, text="clique aqui")
button.place(x=100, y=0)
bt1 = Button(root, text="Teste", command=teste, font="Time 20 bold")

lb1 = Label(root, text="Teste", font="Time 20 bold")
lb1.place(width=80, height=30, x=100, y=400)

root.mainloop()
