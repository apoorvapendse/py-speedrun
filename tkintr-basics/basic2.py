from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry('900x750')
root.title("Appu GUI")

# LABEL ATTRIBUTES:
# bd = background, 
# text =for adding text
# fg = foreground
# font = sets font
# padx = padding along x axis
# pady = padding along y axis
# relief = border styling - SUNKEN,RAISED,GROOVE,RIDGE

# Label is just like div

heading_label = Label(text="Motivation is something that cannot be understood with words but with practice.\nIt means to be moved by something so strongly that it becomes an inspiration for you.\nFurthermore, it is a discipline that helps you to achieve your life goals and also helps to be successful in life.\nBesides, it the most common practice that everyone does whether it is your boss in office or a school teacher or a university professor everyone motivates others in a way or other.",bg="green",fg="white",padx=50,pady=25,font=("cursive",12,"italic") ,borderwidth=5, relief=SUNKEN,)


# pack options
# anchor ="nw","se","ne"(used to align the label) 
# side = top,left,right,bottom , side has to be bottom for south anchors to work 
# fill
# padx
# pady


# heading_label.pack(anchor="s",side="bottom",fill='x');
# to fill in Y side must be either left of right

heading_label.pack(side="left",fill='y')

root.mainloop();