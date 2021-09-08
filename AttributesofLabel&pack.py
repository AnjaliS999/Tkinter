#attributes hume yeh batate hai ki hume kaha pr kaun si chhez ko pack ka
#attributes tells that where to place what type of widget
#like text, images, buttons, checkboxes, etc.

from tkinter import *
root = Tk() #window is created

#to change the title
root.title("My GUI")

#setting options in label and pack
#important label options
# text - adds the text
# bd - background
# fg - foreground
# font -set the font [font=("comicsansms", 19, bold)], [font="comicsansms 19 bold",]
# padx - padding in x
# pady - padding in y
# relief -  border stylingh - SUNKIN , RAISED, GROOVE, RIDGE

title_label = Label(text='''A queue can be defined as an ordered list which enables insert operations to be performed at one end called REAR and delete operations to be performed at another end called FRONT.\n2. Queue is referred to be as First In First Out list.\n3. For example, people waiting in line for a rail ticket form a queue.''',bg = "red", fg = "white",padx = 23, pady = 24, font=("comicsansms", 19, "bold"),  borderwidth=3,relief=SUNKEN)
#goto documentation for more attributes

#important pack options
#ancor = nw, this will move the para in northwest direction of page
#anchor = se, south east
#fill = X & Y, this will fill the texts background and where we willstreth it will fill towars that side only
#padx =
#Pady

# side = top, bottom, left, right, but by default  it is top

title_label.pack(side=BOTTOM, anchor="se", fill=X, pady=34, padx = 12)






title_label.pack()

root.geometry("444x555")

root.mainloop()