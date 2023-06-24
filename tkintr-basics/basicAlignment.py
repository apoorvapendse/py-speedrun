from tkinter import *
root = Tk()

root.geometry('800x700')

frame = Frame(root,bg='red',relief=SUNKEN,borderwidth=4,padx=22)
frame.pack(side=LEFT,anchor='n',fill='y');

frameHeading = Frame(root,bg="green",relief=SUNKEN,pady=20)
frameHeading.pack(side=TOP,anchor='n',fill='x')

l1 = Label(frame,text="hello world");
l1.pack(side=LEFT)

l2 = Label(frameHeading,text="this is heading");
l2.pack(side=TOP)


root.mainloop();