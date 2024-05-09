from tkinter import *


def click():
    no = "python"
    num.delete(0, END)
    num.insert(0, no)


def click2():
    no1 = "Java"
    num.delete(0, END)
    num.insert(0, no1)


def click3():
    no2 = "R"
    num.delete(0, END)
    num.insert(0, no2)


root = Tk()
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)


lbl = Label(root, text="Select the Language you want", font="comicsansms 15", bg="yellow", fg="red", bd="4", relief="solid")
lbl.pack()

num = Entry(root)
num.place(x=190, y=50)

btnpy = Button(root, text="Python", command=click)
btnjv = Button(root, text="Java", command=click2)
btnr = Button(root, text="R", command=click3)


btnpy.place(x=220, y=90)
btnjv.place(x=227, y=130)
btnr.place(x=235, y=170)


root.mainloop()

