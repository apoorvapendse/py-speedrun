from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("appu menu")

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
root.geometry("800x800")

def fileClick():
    print("file button clicked")

def help():
   val = tmsg.showinfo("Help","God helps those who help themselves")


def rate():
    val = tmsg.askyesno("Did you like my program","Please be honest")
    print(val);
    if val==TRUE:
        tmsg.showinfo("Thanks a lot","I am flattered😊")
    else:
        tmsg.showinfo("","Thanks for being honest")

# for non-dropdown menu
# myMenuBar = Menu(root)
# myMenuBar.add_command(label="File",command=fileClick)
# myMenuBar.add_command(label="Exit",command=quit)
# root.config(menu=myMenuBar)

myMenuBar = Menu(root,bg='black',foreground='white');

innerMenu = Menu(myMenuBar,tearoff=0,bg='black',foreground='white');
innerMenu.add_command(label="New",command=fileClick)
innerMenu.add_command(label="Open",command=fileClick)
innerMenu.add_command(label="Save",command=fileClick)
innerMenu.add_command(label="Exit",command=quit)

innerMenu2 = Menu(myMenuBar,tearoff=0,bg='black',foreground='white');
innerMenu2.add_command(label="New2",command=fileClick)
innerMenu2.add_command(label="Open2",command=fileClick)
innerMenu2.add_command(label="Save2",command=fileClick)
innerMenu2.add_command(label="Exit2",command=quit)

innerMenu3 = Menu(myMenuBar,tearoff=0,bg='black',foreground='white');
innerMenu3.add_command(label="Help",command=help)
innerMenu3.add_command(label="About",command=fileClick)
innerMenu3.add_separator();
innerMenu3.add_command(label="FAQs",command=fileClick)
innerMenu3.add_command(label="Rate",command=rate)



myMenuBar.add_cascade(label="File",menu=innerMenu);
myMenuBar.add_cascade(label="Edit",menu=innerMenu2);
myMenuBar.add_cascade(label="Help",menu=innerMenu3);

root.config(menu=myMenuBar);



root.mainloop()