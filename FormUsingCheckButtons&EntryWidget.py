from tkinter import *

root = Tk()
root.title("Sharma Travells")

def getvals():
    print("Submitting Form")

    print(f"{NameValue.get(), PhoneNoValue.get(),GenderValue.get(), PaymentModeValue.get(),EmailValue.get(), FoodServiceValue.get()}")

    #logic for the submission of form
    with open("records.txt", "a") as f: #a is for append mode
        
        f.write(f"{NameValue.get(), PhoneNoValue.get(),GenderValue.get(), PaymentModeValue.get(),EmailValue.get(), FoodServiceValue.get()}")
        
root.geometry("644x333")
#Heading
Label(root, text="Welcome to Sharma Traveller's", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
#entry, text for our form
Name = Label(root, text="Name")
PhoneNo = Label(root, text="PhoneNo.")
Gender = Label(root, text="Gender")
PaymentMode = Label(root, text="PaymentMode")
Email = Label(root, text="Email")

#Pack text for our form
Name.grid(row=1, column=2)
PhoneNo.grid(row=2, column=2)
Gender.grid(row=3, column=2)
PaymentMode.grid(row=4, column=2)
Email.grid(row=5, column=2)


#Tkinter Variables for our storing entries
NameValue = StringVar()
PhoneNoValue = StringVar()
GenderValue = StringVar()
PaymentModeValue = StringVar()
EmailValue = StringVar()
FoodServiceValue = IntVar()

#Entries for our form
NameEntry = Entry(root, textvariable=NameValue)
PhoneNoEntry = Entry(root, textvariable=PhoneNoValue)
GenderEntry = Entry(root, textvariable=GenderValue)
PaymentModeEntry = Entry(root, textvariable=PaymentModeValue)
EmailEntry = Entry(root, textvariable=EmailValue)
FoodServiceEntry = Entry(root, textvariable=FoodServiceValue)

#packing the entries
NameEntry.grid(row=1, column=3)
PhoneNoEntry.grid(row=2, column=3)
GenderEntry.grid(row=3, column=3)
PaymentModeEntry.grid(row=4, column=3)
EmailEntry.grid(row=5, column=3)
# FoodServiceEntry.grid(row=5, column=3)

#checkbox, to create a check box , we nwd to have a checkbox button
#Checkbox and packing it
FoodService = Checkbutton(text="Do you want to Book your Meals?", variable = FoodServiceValue)
FoodService.grid(row=6, column=3)

#Button ad packing it and assigning it a command
Button(text="Submit to Sharma Travels", command=getvals).grid(row=7, column=3)
root.mainloop()


