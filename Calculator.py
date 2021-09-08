from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")#it will give that button which we have clicked
    #and from cget we can get text
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())#eval evaluates string
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.title("Calculator")
root.geometry("333x600")
root.wm_iconbitmap("Calculator-icon.ico")

#creating Frame before it create string val

scvalue = StringVar()
scvalue.set("") #initially set value to the string name scvalue
#entry widget
screen = Entry(root, textvar=scvalue, font="lucida 18 bold")
screen.pack(fill=X, ipadx=4, pady=18, padx=18)


#creating frames, inside which we are gonna pack 3 buttons

f = Frame(root, bg="grey")
b = Button(f, text="1", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="7", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=15, pady=12, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=15, pady=12, font="lucida 16 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=15, pady=12, font="lucida 16 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="*", padx=15, pady=12, font="lucida 16 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=15, pady=12, font="lucida 16 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=15, pady=12, font="lucida 16 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="%", padx=14, pady=12, font="lucida 14 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=14, pady=12, font="lucida 14 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=14, pady=12, font="lucida 14 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()