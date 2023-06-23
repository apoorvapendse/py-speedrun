from tkinter import *
from PIL import Image,ImageTk

root = Tk()
# creates bear minimum gui

# widthxheight
root.geometry("1200x800")

heading = Label(text="appu's gui app")
heading.pack();

image = Image.open("appu.jpeg")
photo = ImageTk.PhotoImage(image)


#width,height
root.minsize(500,300)

root.mainloop()