from  tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("GUI")
canvasWidget = Canvas(root, width=canvas_width, height=canvas_height)
canvasWidget.pack()

#the line goes from the point x1, y1 to x2, y2
canvasWidget.create_line(0, 0, 800, 400, fill="red")
canvasWidget.create_line(0, 400, 800, 0, fill="red")

#To create a rectangle specifr parameters in this order-  coordinates of top
#left and coordinates of bottom right

canvasWidget.create_rectangle(3, 50, 55, 6, fill="blue")

#creating a text or fit it in GUI
canvasWidget.create_text(200, 200, text="Python")

canvasWidget.create_oval(5, 60, 66, 15, fill="yellow")

root.mainloop()