from tkinter import *
root = Tk()
root.title("appu menu")
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
root.geometry("800x800")

def fileClick():
    print("file button clicked")

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


myMenuBar.add_cascade(label="file",menu=innerMenu);
myMenuBar.add_cascade(label="edit",menu=innerMenu2);

root.config(menu=myMenuBar);



root.mainloop()