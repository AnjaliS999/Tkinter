from tkinter import*
# root = Tk()
# root.title("Classes And Objects")
# root.geometry("777x777")
#
# class GUI(Tk):
#
# root.mainloop()

# GUI class Inherited from Tk
class GUI(Tk):
    #constructor in class
    def __init__(self):
        #calling constructor of superclass , this is done because super class,
        # tk its constructor is always called when root = Tk() was to be written

        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print("Button clicked")


    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()
# main function
if __name__ == '__main__':
    # gui class ka object
    window = GUI()
    window.status()
    window.createbutton("Click Me")
    window.mainloop()