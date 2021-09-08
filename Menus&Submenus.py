from tkinter import*
import tkinter.messagebox as tmsg

def myFunc():
    print("This is my new function")

def mySet():
    print("This is a new setting")

def Access():
    print("This is new accessories")

def Help():

    print("I'll help you")
    a = tmsg.showinfo("Help", "I will help you in this GUI")
    print(a)#return value

def rate():
    print("Rate Us")
    value = tmsg.askquestion("Was your experience?")
    if value == "yes":
        msg = "Great. Rate us on Play Store please."
    else:
        msg = "Tell us what went wrong, we will call you soon."
    tmsg.showinfo("Experience", msg)

def NewFriend():
    ans = tmsg.askretrycancel(" Make NewFriend", "Authenticating request")
    if ans:
        print("Retry to make NewFriend")
    else:
        print("Cancelled Request")
root = Tk()
root.geometry("433x500")
root.title("PyCharm")

#use these command to create non dropdown menu
# myMenu = Menu(root)
# myMenu.add_command(label="File", command=myFunc)
# myMenu.add_command(label="Settings", command=mySet)
# myMenu.add_command(label="Accessories", command=Access)
# myMenu.add_command(label="Exit", command=quit)
#Generally, command is not added, we will do this by dropdown menu

mainMenu = Menu(root)
m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label="New Project", command=myFunc)
m1.add_command(label="Save", command=mySet)
m1.add_separator()
m1.add_command(label="Save As", command=Access)
m1.add_command(label="Print", command=myFunc)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Copy", command=mySet)
# m2.add_separator()
m2.add_command(label="Paste", command=Access)
m2.add_command(label="Find", command=myFunc)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainMenu, tearoff=0)
m3.add_command(label="Getting Started", command=myFunc)
m3.add_command(label="Submit Feed Back", command=mySet)
# m3.add_separator()
m3.add_command(label="Edit Custom", command=Access)
m3.add_command(label="Help?", command=Help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Be Friend GUI", command=NewFriend)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Help", menu=m3)

root.config(menu=mainMenu)
root.mainloop()