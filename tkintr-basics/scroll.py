from tkinter import *

root = Tk();
root.geometry("800x800");
root.title("Scroll")
# connecting scrollbar to a widget 
# widget(yscrollcommand = scrollbar.set)
# scrollbar.config(command = widget.yview)
scrollbar = Scrollbar(root)
listbox = Listbox(root,yscrollcommand=scrollbar.set)
scrollbar.pack(fill=Y,side=RIGHT);
for i in range(100):
    listbox.insert(END,f"obj{i}")


scrollbar.config(command=listbox.yview)
listbox.pack()


root.mainloop();