from tkinter import *
root = Tk();
root.geometry("800x700")


def submit():
   
    print(namevalue.get())
    print(passvalue.get())


# entry widget is similar to input tag

l1=Label(root,text="Username:")
l2=Label(root,text="Password:")

# row = 0 , col = 0 is default
l1.grid()
l2.grid(row=1)

# Variable Classes in tkinter 
# BooleanVar,DoubleVar,StringVar,IntVar
namevalue = StringVar()
passvalue = StringVar()

userName = Entry(root,textvariable=namevalue).grid(row=0,column=1)
userPass = Entry(root,textvariable=passvalue).grid(row=1,column=1)

submitBtn = Button(text='Submit', command = submit)
submitBtn.grid(row=2)

root.mainloop();