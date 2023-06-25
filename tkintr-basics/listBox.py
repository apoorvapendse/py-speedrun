from tkinter import *
root = Tk()
root.geometry("899x777")
root.title("listbox")

def add():
    task = item.get()
    lbx.insert(END,task);
def delete():
    selectedItem = lbx.curselection()
    lbx.delete(selectedItem)
lbx= Listbox(root,width=40,height=12)
lbx.insert(END,"First Item")

lbx.pack()


item = StringVar()
itemEntry = Entry(root,textvariable=item)
itemEntry.pack()


Button(text="Add Item",command=add).pack()
Button(text="delete item",command=delete).pack()

root.mainloop()

