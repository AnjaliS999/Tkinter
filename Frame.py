#FRAMES/BORDER
# The Frame widget is very important for the process of grouping and organizing other widgets in a somehow friendly way.
# It works like a container, which is responsible for arranging the position of other widgets.
#
# It uses rectangular areas in the screen to organize the layout and to provide padding of these widgets.
# A frame can also be used as a foundation class to implement complex widgets.
from tkinter import *
root = Tk()
root.geometry("655x333")
#frame
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")#this will make a frame on the left side

f2 = Frame(root, borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")
#creating label

l = Label(f1, text="PyCharm")#label inside f1
l.pack(pady=142)
l = Label(f2, text="SublimeText", font="Helvetica 16 bold", fg="red", pady=22 )#label inside f1
l.pack()
root.mainloop()