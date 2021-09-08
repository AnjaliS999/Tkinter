from tkinter import *

def Fun(event):
    print(f"You clicked on the button at {event.x}, {event.y}")#by doing this event is being handled

root = Tk()
root.title("Events In Tkinter")
root.geometry("644x333")
widget = Button(root, text='Click me Please')
widget.pack()
#Handling events in Tkinter [events- searching, cpy, moving cursor all these are events
#binding events

widget.bind('<Button-1>', Fun) #if we press button the Fun calls
widget.bind('<Double-1>', quit)#by double click the button , the whole program is terminated

root.mainloop()