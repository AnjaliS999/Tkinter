from tkinter import *
root = Tk()
root.geometry("645x333")

def Btn():
    print("This is a Tkinter Button")

def World():
    print("Enter to the Tkinter's World")

def Greetings():
    print("Welcome to the Tkinter World")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print", padx=12, command=Btn)
b1.pack(side=LEFT, padx=44)
b2 = Button(frame, fg="green", text="OK", command=World)
b2.pack(side=LEFT, padx=44)
b3 = Button(frame, fg="yellow", text="Cancel", command=Greetings)
b3.pack(side=LEFT, padx=44)
root.mainloop()