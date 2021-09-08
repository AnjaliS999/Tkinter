from tkinter import *

def getvals():
    print(Uservalue.get())
    print(Passwordvalue.get())

root = Tk()
root.geometry("644x333")
#GridLayout

User = Label(root, text="UserName")
Password = Label(root, text="Password")

User.grid()
Password.grid(row=1)

#EntryWidget, in which we can add values to it , same as text area
#Variable Classes in TKinter

# BooleanVar, DoubleVar, IntVar, StringVar
# StringVar - put it in entry class

Uservalue = StringVar()
Passwordvalue = StringVar()

Userentry = Entry(root, textvariable = Uservalue)
Passwordentry = Entry(root, textvariable = Passwordvalue)

#Now pack them with thw help of grid

Userentry.grid(row=0, column=1)
Passwordentry.grid(row=1, column=1)

#now create a button

Button(text="Submit", command=getvals).grid()

root.mainloop()