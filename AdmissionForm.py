from tkinter import *

def getvals():
    print(StudentVal.get())
    print(FatherVal.get())
    print(AgeVal.get())

root = Tk()
root.geometry("650x333")

Student = Label(root, text="Student's Name:")
Father = Label(root, text="Father's Name:")
Age = Label(root, text="Student's Age:")



Student.grid()
Father.grid(row=1)
Age.grid(row=2)

StudentVal = StringVar()
FatherVal = StringVar()
AgeVal = StringVar()

StudentEntry = Entry(root, textvariable = StudentVal)
FatherEntry = Entry(root, textvariable = FatherVal)
AgeEntry = Entry(root, textvariable = AgeVal)

StudentEntry.grid(row=0, column=1)
FatherEntry.grid(row=1, column=1)
AgeEntry.grid(row=2, column=1)

Button(text="Press", command=getvals).grid()

root.mainloop()