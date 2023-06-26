from tkinter import *

root = Tk();
root.geometry("800x800")

def updateHandler():
    import time;
    val.set("Busy...")
    statusBar.update()
    time.sleep(2);
    val.set("READY")

val = StringVar();
val.set("ready")
statusBar = Label(root,relief=SUNKEN,textvariable=val,pady=12,padx=12,anchor='sw')
statusBar.pack(side=BOTTOM,fill=X)

Button(text="Update", command=updateHandler).pack();

root.mainloop();