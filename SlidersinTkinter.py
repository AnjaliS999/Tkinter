from tkinter import*
#message box
import tkinter.messagebox as tmsg
root = Tk()


def getDollar():
    print(f"We have credited {mySlider.get()} Dollars to your bank account.")
    tmsg.showinfo("Amount Credited!", f"We have credited {mySlider.get()} Dollars to your bank accoumnt")


root.title("Silder")
root.geometry("555x777")

#vertical Slider
mySlider = Scale(root, from_=0, to=111)
mySlider.pack()

#label
Label(root, text="How many dollars you want?").pack()
#horizontal Slider
mySlider2 = Scale(root, to=100, orient= HORIZONTAL, tickinterval=50)
mySlider2.set(24)
mySlider2.pack()
Button(root, text="Get Dollars!",pady=10, command= getDollar).pack()

root.mainloop()