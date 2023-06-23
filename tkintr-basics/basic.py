from tkinter import *
from PIL import Image,ImageTk

root = Tk()
# creates bear minimum gui

# widthxheight
root.geometry("900x700")

heading = Label(text="appu's gui app")
heading.pack();

image = Image.open("appu.jpeg")

newSize = (400,300)
resizedImage = image.resize(newSize)

photo = ImageTk.PhotoImage(resizedImage)

image_label = Label(root, image=photo)
image_label.pack()
#width,height
root.minsize(500,300)

root.mainloop()