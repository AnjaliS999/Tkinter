# image is also a widget in which user is not directly interactive


from tkinter import *
from PIL import Image, ImageTk
#we have a function inside this which helps to take a jpg file in tkinter
#Tkinter does not support jpg so




resume_root = Tk()
#images
resume_root.geometry("200x244")
# photo = PhotoImage(file="A.png")

#For JPG Images
image = Image.open("m.jpg")
photo = ImageTk.PhotoImage(image)
#This(photo = ImageTk.PhotoImage) was used before from PIL import Image, ImageTk

new_Label = Label(image=photo)
new_Label.pack()


resume_root.mainloop()

#download pillow module by using pip install pilow in terminal , pillow means python imaging libary

