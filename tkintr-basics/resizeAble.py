#TODO:Create a gui window that takes input for width and height and upon clicking apply, it should be able to change its size accordingly
from tkinter import *
root = Tk()
root.geometry("700x600")

def resizeWindow():
    newWidth = widthOfScreen.get()
    newHeight = heightOfScreen.get()
    root.geometry(f"{newWidth}x{newHeight}")
    widthOfScreen.set("")
    heightOfScreen.set("")

widthLabel = Label(root,text="enter width");
heightLabel = Label(root,text="enter height");

widthLabel.grid(row=0,column=0)
heightLabel.grid(row=1,column=0)


widthOfScreen = StringVar()
heightOfScreen = StringVar()

widthEntry = Entry(root,textvariable=widthOfScreen).grid(row=0,column=1)
heightEntry = Entry(root,textvariable=heightOfScreen).grid(row=1,column=1)
applyBtn = Button(root,text="apply",command=resizeWindow).grid()


root.mainloop()