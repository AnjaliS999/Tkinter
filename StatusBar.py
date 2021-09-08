from tkinter import *

def upload():
    statusvar.set("Busy.....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

root = Tk()
root.title("StatusBar")
root.geometry("333x555")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable =statusvar, relief=SUNKEN, anchor="w")
Button(root, text="Upload", command=upload).pack()
sbar.pack(side=BOTTOM, fill=X)


root.mainloop()