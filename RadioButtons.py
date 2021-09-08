from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def Order():
    tmsg.showinfo("Order Recieved!", f"We have recieved your order for { var.get()}. Thanks for Ordering")

root.title("Radio Button")
root.geometry("666x777")
#declare variable
# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)

Label(root, text="What would you like to have Sir?",font="lucida 19 bold", justify=LEFT, padx=14).pack()
#options

radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack( anchor="w")
radio = Radiobutton(root, text="AluParatha", padx=14, variable=var, value="AluParatha").pack( anchor="w")
radio = Radiobutton(root, text="MatarPaneer", padx=14, variable=var, value="MatarPaneer").pack( anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack( anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack( anchor="w")


#how to retrive value

Button(text="Order Now", command=Order).pack()



root.mainloop()