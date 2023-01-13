from tkinter import *
import random
import pyperclip



def display():
    entry.delete(0, END)

    length = val.get()

    password = ""
    uppercase_letters = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    numbers = "0123456789"
    symbols = "(){}[],:;.-/\?+&#*"

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lowercase_letters)
        return password

    elif var.get() == 2:
        for i in range(0, length):
            password = password + random.choice(lowercase_letters + uppercase_letters)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(lowercase_letters + uppercase_letters + numbers)
        return password
    
    elif var.get() == 4:
        for i in range(0, length):
            password = password + random.choice(lowercase_letters + uppercase_letters + numbers + symbols)
        return password
    else:
        print("Hello")
    
def button_press():
    total_password = display()
    entry.insert(0, total_password)

def copy():
    copy_password = entry.get()
    pyperclip.copy(copy_password)

window = Tk()

var = IntVar()
val = IntVar()

entry = Entry(window, width=30,bd=2)
entry.pack()

r1 = Radiobutton(text="Weak", variable=var, value=1).pack()
r2 = Radiobutton(text="Medium", variable=var, value=2).pack()
r3 = Radiobutton(text="Strong", variable=var, value=3).pack()
r4 = Radiobutton(text="Extreme", variable=var, value=4).pack()

spin1 = Spinbox(window, from_=1, to=25, textvariable=val, width=20,)
spin1.pack()


button1 = Button(window, text="Generate Password", height=5, width=25, bg="white", command=button_press)
button1.pack()

button2 = Button(window, text="Copy", height=5,width=25,bg="white",command=copy)
button2.pack()



window.mainloop()