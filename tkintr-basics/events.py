from tkinter import *
root = Tk();
root.title("events");
root.geometry("800x600")
def appu(e):
    print(f"You Clicked at {e.x} and {e.y}")
    

widget = Label(text="hello i am widget",borderwidth=3,bg='red');
# Button-1 event means mouse is click once over it 
widget.bind("<Button-1>",appu)
widget.bind("<Double-1>",quit)
widget.pack()



root.mainloop()