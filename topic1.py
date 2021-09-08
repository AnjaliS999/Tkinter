# from tkinter import *
# here we are importing every module form the above which is not a good practice

# varName_root = Tk() # This is root and this will form the basic GUI , by doing our (basic components
# are present) this our base is created and we can add many menubar widgets etc and get back to main
# loop

# root is an instance of a class Tk()
# ctrl+clickOn Tk(), we will get all the implementation of the class Tk

# Logic of GUI
# come to the event loop using mainloop()

# after applying all the widgets to it we go to mainloop
# varName_root.mainloop()  #with the help of this main loop it keeps in GUI
# window and  makes it interactive, and reminds the logic that has been used


#Tkinter is Python’s standard GUI (Graphical User Interface) package. tkinter provides us with a
# variety of common GUI elements which we can use to build out interface – such as buttons, menus
# and various kind of entry fields and display areas. We call these elements Widgets.


#Widget is an element of Graphical User Interface (GUI) that displays/illustrates information or
# gives a way for the user to interact with the OS.  In Tkinter , Widgets are objects ; instances
# of classes that represent buttons, frames, and so on.

#Each separate widget is a Python object. When creating a widget, you must pass its parent as a
# parameter to the widget creation function. The only exception is the “root” window, which is the
# top-level window that will contain everything else and it does not have a parent.
#example
from tkinter import *

# create root window
root = Tk()

# frame inside root window
frame = Frame(root)

# geometry method
frame.pack()

# button inside frame which is
# inside root
button = Button(frame, text='Anjali')
button.pack()

# Tkinter event loop
root.mainloop()
#