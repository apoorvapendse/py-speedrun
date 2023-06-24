from tkinter import *


def b1():
    print("you clicked button1")
    print()

def b2():
    print("you clicked button2")
    print()
    
def b3():
    print("you clicked button3")
    print();
def b4():
    print("you clicked button4")
    print()

root = Tk()
root.geometry("800x700")


frame = Frame(root,bg="red", borderwidth=3)
frame.pack(side='left',anchor='nw')




b1 = Button(frame,text="Button1", command=b1)
b1.pack(side=TOP)

b2 = Button(frame,text="Button2" ,command=b2)
b2.pack(side=TOP)

b3 = Button(frame,text="Button3" ,command=b3)
b3.pack(side=TOP)

b4 = Button(frame,text="Button4", command=b4)
b4.pack(side=TOP)

root.mainloop() 