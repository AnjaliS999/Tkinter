#label-> a widget which is not interacted by a user and It is used
# to display text or image on the screen.

#we can handle the size of our geometry, small, large or we can lock it as well.
# Creating a new widget doesn’t mean that it will appear on the screen. To display it,
# we need to call a special method: either grid, pack(example above), or place and all
# these comes under geometry management

from tkinter import *

root = Tk()
#order of geometry = width* height
root.geometry("644x434")#geometry is a function which is kickstart of a gui.
#by using geometry with width and height arguments in it we can resize the
# window size and for some resone we want limited size max and min

root.minsize(100,400)#it will take arguments as width, height
# root.maxsize(200,800)#it will take arguments as width, height

#using Label
new = Label(text="A label is formed but it will not display anything in the GUI" 
                 " and to display this text in GUI we need to pack our variable by using "
                 "Pack() function")

new.pack()
root.mainloop()
#from
# from tkinter import *
#root = Tk()
#root.mainloop()
# these three lines we will get our basic window which is blank and later
# we will do all the coding inside it







